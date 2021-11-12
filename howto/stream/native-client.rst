.. _howto_stream_native-client:

=========================
Implement a native client
=========================

This native SDK contains a header file to include in your C or C++ based
program and the shared library to link against.

To integrate the native SDK to your program. You need to initialize
AnboxStreamConfig object first, and set the concrete config items via
the object.

.. code:: bash

       std::unique_ptr<AnboxStreamConfig, void(*)(AnboxStreamConfig*)> cfg(
         anbox_stream_config_new(),
         [](AnboxStreamConfig* cfg) { anbox_stream_config_release(cfg); });

       // The SDK does handle the signaling process for us. All we have to do is
       // to tell it the URL of the signaling endpoint
       EXIT_ON_FAILURE(anbox_stream_config_set_signaling_url(cfg.get(), session_url));
       EXIT_ON_FAILURE(anbox_stream_config_set_use_insecure_tls(cfg.get(), use_insecure_tls));
       EXIT_ON_FAILURE(anbox_stream_config_add_stun_server(cfg.get(), stun_server_urls, size_of_urls, username, password));

After all configurations are set you can create the Anbox Stream object.
You probably need to hold the stream by a custom context object as the
stream is required for a few other functions to be invoked later on.

.. code:: bash

       Context ctx;
       ctx.stream = anbox_stream_new(cfg.get());

Then in order to monitor the WebRTC peer connection state, disconnection
signal, or error occurring during streaming. The following callback
functions are expected to be registered. Those callback functions accept
a valid anbox stream object that is created above.

.. code:: bash

       EXIT_ON_FAILURE(anbox_stream_set_connected_callback(ctx.stream, [](void* user_data) {
           auto ctx = reinterpret_cast<Context*>(user_data);
           # Start rendering thread after streaming gets connected.
       }, &ctx));


       EXIT_ON_FAILURE(anbox_stream_set_disconnected_callback(ctx.stream, [](void* user_data) {
          auto ctx = reinterpret_cast<Context*>(user_data);
          # Release the resource when streaming get disconnected.
       }, &ctx));


       EXIT_ON_FAILURE(anbox_stream_set_error_callback(ctx.stream, [](AnboxStatus status, void* user_data) {
          # Respect the status and run error handling routine.
       }, nullptr));

To capture the audio output data and playout on the client side. You
need to register the following function and process the received PCM
audio data via platform specific API for playback

.. code:: bash

       EXIT_ON_FAILURE(anbox_stream_set_audio_data_ready_callback(ctx.stream, [](
           const uint8_t* audio_data, size_t len, void *user_data){
         auto ctx = reinterpret_cast<Context*>(user_data);
         # Process PCM audio data for playback
       }, &ctx));

After all set, you can call the following function to connect the stream

.. code:: bash

       EXIT_ON_FAILURE(anbox_stream_connect(ctx.stream));

To forward input events occurring on the client to the Android
container, you need to construct the ``AnboxStreamControlMessage`` based
on actual input event via platform specific API.

::

         AnboxStreamControlMessage msg;
         memset(&msg, 0, sizeof(msg));

         ```
            # Construct control message according to different platform API
         ```
         anbox_stream_send_message(ctx.stream, &msg);

In the user defined render thread, it’s expected to set proper viewport
size and render each frame immediately once a frame is available.

.. code:: bash


   void run_render_thread(Context* ctx) {
     ...
     ...
     eglMakeCurrent(display, surface, surface, context);

     while (ctx->running) {
       anbox_stream_set_viewport_size(ctx->stream.get(), width, height);
       anbox_stream_render_frame(ctx->stream.get(), 100);
       eglSwapBuffers(display, surface);
     }
   }

And when streaming is done, the client is in charge of releasing the
Anbox stream object.

.. code:: bash

       EXIT_ON_FAILURE(anbox_stream_release(ctx.stream));
