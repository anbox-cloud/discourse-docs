# Client Side Virtual Keyboard

The Anbox Streaming SDK enables developers to build a hybrid mobile application that can integrate the features that Anbox Cloud provides. It comes with an [Android library](https://developer.android.com/studio/projects/android-library) that offers easy-to-use native components like AnboxWebView, which you can use to quickly integrate a client-side virtual keyboard feature into your mobile application. This client-side virtual keyboard can send text to the Android container on the fly when typing.

The AnboxWebView extends the AOSP [WebView](https://developer.android.com/reference/android/webkit/WebView). It provides better handling of the text input for the hybrid application that loads the Anbox Streaming JavaScript SDK with an embedded WebView for video streaming.

## Import the AAR library

Check out the [Anbox Streaming SDK](https://github.com/anbox-cloud/anbox-streaming-sdk) from GitHub:

    git clone https://github.com/anbox-cloud/anbox-streaming-sdk.git

The `android/libs` folder contains the `com.canonical.anbox.streaming_sdk.aar` AAR file. See the official [documentation](https://developer.android.com/studio/projects/android-library) for how to import an Android library into an Android application project.
The `examples/android` folder contains the `enhanced_webview_streaming` Android application. Refer to this application as an example for this feature integration.

## Integrate components

After importing the AAR file, use the AnboxWebView in an Android project:
1. Adjust the layout of the activity XML file that you want to use for the AnboxWebView component. For example:

   ```
    <com.canonical.anbox.streaming_sdk.AnboxWebView
        android:id="@+id/webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
   ```

2. Use the [addJavascriptInterface](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface) method to inject a Java object `AppInterface` into the AnboxWebView. This object acts as a bridge that provides access from JavaScript to the Android Java layer.

   ```
   import com.canonical.anbox.streaming_sdk.AnboxWebView;
   ...

   public class MainActivity extends AppCompatActivity {
       protected void onCreate(Bundle savedInstanceState) {
           ...
           mWebview = (AnboxWebView) findViewById(R.id.webview);
           mWebView.addJavascriptInterface(new AppInterface(this), "AppInterface");
           ...
       }
   }
   ```

3. For the application running in the Android container, whenever a text editor gains or loses focus during streaming, an IME-specific message is sent from the Android container to the client through the Javascript SDK. Each message requests a certain IME operation. This allows you to perform one certain action when the message is received and ensures the behaviour of the virtual keyboard is synced on both ends. The supported IME messages are as follows:

   The following IME messages are supported:

    Message          |  Description
    -----------------|-----------------------------------------------
    show-ime         |  Request to show client-side virtual keyboard
    hide-ime         |  Request to hide client-side virtual keyboard

    To receive the above messages, register the `messageReceived` callback function when instantiating an AnboxStream object in HTML. Through the injected Java object `AppInterface`, the client-side virtual keyboard will pop up or hide when the corresponding message is received.

   ```
       window.stream = new AnboxStream({
           ...
           ...
           ...
           callbacks: {
               ...
               ...
               messageReceived: (type, data) => {
                   switch(type) {
                   case "show-ime" :
                       AppInterface.openVirtualKeyboard();
                   break;
                   case "hide-ime" :
                       AppInterface.hideVirtualKeyboard();
                   break;
                   default:
                       console.log("Unhandled message:" + type)
                   break;
                   }
               }
           }
       });
   ```

4. Set up the listener to the activity where you want to capture the message. You must implement the following methods for the AppInterface.ActionListener interfaces so that the application will be notified when a request is coming from the JavaScript SDK.

   ```
   public class MainActivity extends AppCompatActivity implements AppInterface.ActionListener {
   ...

       /**
        * Called as the request to open virtual keyboard
        */
       @Override
       public void onOpenVirtualKeyboard() {
       }

       /**
        * Called as the request to hide virtual keyboard
        */
       @Override
       public void onHideVirtualKeyboard() {
       }

   ```

5. Set up the listener to the activity for which you want to capture the text input events from the virtual keyboard or monitor its visibility changes during streaming.

   ```
   import com.canonical.anbox.streaming_sdk.AnboxWebView;
   ...

   public class MainActivity extends AppCompatActivity implements AnboxWebView.VirtualKeyboardListener, AppInterface.ActionListener {
   ...
       protected void onCreate(Bundle savedInstanceState) {
           ...
           mWebview = (AnboxWebView) findViewById(R.id.webview);
           mWebview.setVirtualKeyboardListener(this);
           ...
       }
   ```

   When people start typing, one of the following methods from the AnboxWebView.VirtualKeyboardListener interfaces will be triggered:

   ```
       /**
        * Called as text is committed from the virtual keyboard.
        *
        * @param text the committed text displayed in the text editor after its composing state
        *        is cleared.
        * @note  text is not the whole visual characters displaying in the text editor, instead it's
        *        just the new text appended to the current existing text after finishing composing.
        *
        */
       @Override
       public void onVirtualKeyboardTextCommitted(String text) {
       }

       /**
        * Called as text is being composing from the virtual keyboard.
        *
        * @param text the composing text displayed in the virtual keyboard.
        * @note  There might be no composing state for some CJK language based IMEs, hence
        *        this function may not be called at all for those languages in some IMEs.
        *
        */
       @Override
       public void onVirtualKeyboardTextComposing(String text) {
       }

       /**
        * Called as input text is deleted from the current text editor.
        *
        * @param counts the number of characters that are deleted before the current cursor position.
        */
       @Override
       public void onVirtualKeyboardTextDeleted(int counts) {
       }

       /**
        * Called as the region of composing text is changed.
        *
        * @param start the position in the text at which the composing region begins.
        * @param end the position in the text at which the composing region ends.
        */
       @Override
       public void onVirtualKeyboardComposingTextRegionChanged(int start, int end) {
       }

       /**
        * Called as the state of the virtual keyboard is changed.
        *
        * @param visible the visibility of the virtual keyboard, true or false.
        * @param heightRatio the ratio of virtual keyboard's height to screen when virtual keyboard is visible.
        *        This can be used to notify the IME running in the Android container
        *        to adjust the display height to honor the virtual keyboard display
        *        ratio on the client side.
        *
        */
       @Override
       public void onVirtualKeyboardStateChanged(boolean visible, double displayRatio) {
       }

   ```

6. In your HTML, define the JavaScript functions that can be invoked from the Android Java layer(AnboxWebView). Those functions are just wrappers of the APIs that are exposed from the JavaScript SDK. This builds up a communication tunnel that works the other way around.
   ```
   <script>
     function sendIMECommittedText(text) {
       window.stream.sendIMECommittedText(text);
     }
     function sendIMEComposingText(text) {
       window.stream.sendIMEComposingText(text);
     }
     function sendIMETextDeletion(counts) {
       window.stream.sendIMETextDeletion(counts);
     }
     function sendIMEAction(name, params) {
       window.stream.sendIMEAction(name, params);
     }
     function sendIMEComposingRegion(start, end) {
       window.stream.sendIMEComposingRegion(start, end);
     }
   </script>

   ```

7. Once the virtual keyboard pops up on the client side, the `onVirtualKeyboardStateChanged` callback function is triggered. To keep the display proportions correct for IME displaying on both the client and the server ends, the `show` action, which carries the display ratio, must be sent out to the server side.

   ```
       @Override
       public void onVirtualKeyboardStateChanged(boolean visible, double displayRatio) {
           if (visible == true) {
               String action = "show";
               String params = "height-ratio=" + displayRatio;
               mWebView.loadUrl(String.format("javascript:sendIMEAction(\"%s\", \"%s\")", action, params));
           }
       }

   ```

8. When typing on the virtual keyboard, a text input event is triggered when one of the following scenarios occurs:
   - A series of characters is committed to a text editor
   - A text is currently being composed
   - A text is being deleted

    In the above cases, the changed text must be sent to the server side through the JavaScript SDK. This can be done by calling JavaScript functions that are defined in HTML through AnboxWebView. For example, for committing text:

   ```
       @Override
       public void onVirtualKeyboardTextCommitted(String text) {
           mWebView.loadUrl(String.format("javascript:sendIMECommittedText(\"%s\")", text));
       }

   ```

The above workflow provides a general overview of how to integrate the client-side virtual keyboard feature into an Android application. For the complete implementation details, refer to the `enhanced_webview_streaming` example in the `example/android` folder.
