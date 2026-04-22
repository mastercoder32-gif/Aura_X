from Disclaimer import show_disclaimer  # استدعاء نظام الأمان الجديد
import os
import time
import sys

# دالة البانر (الواجهة البصرية)
def banner():
    print("""
    \033[1;33m
     █████╗ ██╗   ██╗██████╗  █████╗     ██╗  ██╗
    ██╔══██╗██║   ██║██╔══██╗██╔══██╗    ╚██╗██╔╝
    ███████║██║   ██║██████╔╝███████║     ╚███╔╝ 
    ██╔══██║██║   ██║██╔══██╗██╔══██║     ██╔██╗ 
    ██║  ██║╚██████╔╝██║  ██║██║  ██║    ██╔╝ ██╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝
    [ Aura-X v2.0 | Shielding Your Digital Assets ]
    \033[0m""")

# دالة شريط التقدم لإعطاء لمسة احترافية
def progress_bar(msg, duration):
    print(f"\033[1;34m[*] {msg}\033[0m")
    for i in range(1, 21):
        sys.stdout.write(f'\r\033[1;33m   [{"#"*i}{"."*(20-i)}] {i*5}%\033[0m')
        sys.stdout.flush()
        time.sleep(duration/20)
    print("\n")

# الدالة الأساسية للفحص
def run_scan():
    # طلب الهدف من المستخدم
    target = input("\033[1;32m[?] أدخل رابط الموقع أو IP للفحص: \033[0m")
    
    print(f"\033[1;35m[!] بدء تحليل الهدف: {target}...\033[0m\n")
    
    # المرحلة الأولى: فحص الخدمات باستخدام Nmap
    print("\033[1;33m--- [1/2] جاري فحص الخدمات (Nmap) ---\033[0m")
    os.system(f"nmap -sV -T4 {target}")
    print("-" * 50)

    # المرحلة الثانية: فحص الثغرات باستخدام Nuclei
    print("\033[1;33m--- [2/2] جاري كشف الثغرات (Nuclei) ---\033[0m")
    # تم إضافة فحص شامل للثغرات من Low إلى Critical
    os.system(f"nuclei -u {target} -severity low,medium,high,critical")
    print("-" * 50)
    
    print("\033[1;32m[+] اكتمل الفحص بنجاح! راجع النتائج أعلاه.\033[0m")

# نقطة انطلاق البرنامج
if __name__ == "__main__":
    try:
        # تشغيل إخلاء المسؤولية أولاً
        show_disclaimer() 
        # إذا وافق المستخدم، تظهر الواجهة ويبدأ العمل
        banner()
        run_scan()
    except KeyboardInterrupt:
        print(f"\n\n\033[1;31m[!] تم إغلاق البرنامج بواسطة المستخدم.\033[0m")
        sys.exit()

