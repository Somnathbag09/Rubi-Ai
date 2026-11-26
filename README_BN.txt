RUBI AI — Android APK Starter Project
=====================================

এই ZIP-এ একটি সাধারণ Kivy Android app এবং GitHub Actions build workflow আছে।
এটি সম্পূর্ণ Jarvis/LLM/3D/voice-control app নয়। বর্তমানে chat UI, basic Bengali
responses, time/date এবং local chat history রয়েছে। উন্নত AI, speech recognition,
background wake-word, phone control এবং 3D avatar আলাদা করে নিরাপদভাবে
implement ও test করতে হবে।

GitHub ওয়েবসাইট দিয়ে APK বানানোর নিয়ম (PAT ছাড়াই)
------------------------------------------------
1. https://github.com/new খুলে নতুন Public repository বানান, নাম দিন RUBI-AI।
   README / .gitignore / license auto-add করবেন না।
2. Repository page-এ "uploading an existing file" নির্বাচন করুন।
3. ZIP extract করে ভেতরের সব ফাইল ও .github folder upload করুন।
   .github/workflows/build-apk.yml-ও upload হয়েছে নিশ্চিত করুন।
4. Commit changes চাপুন।
5. Repository-র Actions tab খুলুন। "Build RUBI AI APK" workflow চলবে।
6. Workflow সবুজ হলে run খুলে নিচের Artifacts থেকে RUBI-AI-debug-APK ডাউনলোড করুন।
7. ZIP artifact extract করে APK-তে tap করুন। Android চাইলে এই browser/file manager-এর
   জন্য "Install unknown apps" অনুমতি দিন। শুধুমাত্র নিজের তৈরি APK ইনস্টল করুন।

গুরুত্বপূর্ণ
-----------
- GitHub website-এ upload করলে Termux-এ Git password/PAT দিতে হবে না।
- GitHub Actions-এ প্রথম build 10-30 মিনিট বা তার বেশি লাগতে পারে; failure হলে
  Actions log-এর error দেখে সংশোধন করতে হবে।
- Debug APK Play Store release-এর জন্য signed release build নয়।
- APK-তে কোনো API key রাখবেন না। AI API হলে server-side backend ব্যবহার করুন।
- Android sandbox-এর কারণে arbitrary shell commands বা সম্পূর্ণ phone control
  সাধারণ app থেকে সম্ভব নয়; permissions/Android APIs/Accessibility consent প্রয়োজন।
- এই project Termux-এ `python main.py` চালানোর জন্য নয়; APK build workflow-এর source।
