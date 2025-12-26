import flet as ft

# --- قاعدة بيانات المستخدمين ---
ADMIN_DATABASE = {
    "nour_admin": "2026",
    "student_user": "yasr_ammar",
    "ahmed_hilla": "yASR-AMAR1AA"
}

# --- المواد الدراسية ---
SUBJECTS = {
    "English": {"progress": 0.6, "units": ["Grammar", "Reading", "Writing"]},
    "Math": {"progress": 0.3, "units": ["Algebra", "Geometry", "Calculus"]},
    "Science": {"progress": 0.5, "units": ["Physics", "Chemistry", "Biology"]},
    "History": {"progress": 0.2, "units": ["Ancient", "Medieval", "Modern"]}
}

def main(page: ft.Page):
    page.title = "English Stage 2 - Lord App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {"Poppins": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf"}
    page.theme = ft.Theme(font_family="Poppins")
    
    def show_login():
        page.clean()
        username = ft.TextField(label="اسم المستخدم", autofocus=True, icon=ft.icons.PERSON)
        password = ft.TextField(label="كلمة المرور", password=True, can_reveal_password=True, icon=ft.icons.LOCK)

        def login_click(e):
            user = username.value
            pwd = password.value
            if user in ADMIN_DATABASE and ADMIN_DATABASE[user] == pwd:
                page.snack_bar = ft.SnackBar(ft.Text("✅ تم تسجيل الدخول بنجاح!"))
                page.snack_bar.open = True
                page.update()
                show_dashboard(user)
            else:
                page.snack_bar = ft.SnackBar(ft.Text("❌ اسم المستخدم أو كلمة المرور غير صحيحة!"))
                page.snack_bar.open = True
                page.update()

        page.add(
            ft.Column([
                ft.Text("تسجيل الدخول", size=30, weight="bold"),
                username,
                password,
                ft.ElevatedButton("تسجيل الدخول", on_click=login_click),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        )

    def show_dashboard(user):
        page.clean()
        welcome_text = ft.Text(f"مرحبًا {user}!", size=25, weight="bold")
        subject_buttons = []
        for subject, info in SUBJECTS.items():
            btn = ft.ElevatedButton(
                f"{subject} - {int(info['progress']*100)}%",
                on_click=lambda e, s=subject: show_subject_details(s, user)
            )
            subject_buttons.append(btn)

        theme_toggle = ft.IconButton(
            ft.icons.BRIGHTNESS_4,
            on_click=lambda e: toggle_theme()
        )

        page.add(
            ft.Column([
                ft.Row([welcome_text, theme_toggle], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text(f"عدد المواد: {len(SUBJECTS)}", size=18),
                ft.Column(subject_buttons, spacing=10),
                ft.ElevatedButton("التواصل مع الإدارة", on_click=lambda e: page.launch_url("https://t.me/Yasr_ammar1")),
                ft.ElevatedButton("تسجيل الخروج", on_click=lambda e: confirm_logout())
            ], spacing=15)
        )

    def show_subject_details(subject_name, user):
        page.clean()
        info = SUBJECTS[subject_name]
        units_tabs = [ft.Tab(text=unit, content=ft.Text(f"محتوى الوحدة: {unit}")) for unit in info["units"]]
        page.add(
            ft.Column([
                ft.Text(f"صفحة المادة: {subject_name}", size=22, weight="bold"),
                ft.ProgressBar(value=info["progress"], width=300),
                ft.Tabs(tabs=units_tabs, expand=True),
                ft.Row([
                    ft.ElevatedButton("العودة للرئيسية", on_click=lambda e: show_dashboard(user)),
                    ft.ElevatedButton("مشاركة المادة", on_click=lambda e: page.launch_url(f"https://t.me/Yasr_ammar1?text=Check {subject_name}"))
                ], spacing=10)
            ], spacing=15)
        )

    def toggle_theme():
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def confirm_logout():
        def yes_click(e):
            show_login()
        page.dialog = ft.AlertDialog(
            title=ft.Text("تأكيد الخروج"),
            content=ft.Text("هل تريد تسجيل الخروج فعلاً؟"),
            actions=[
                ft.TextButton("لا", on_click=lambda e: page.dialog.close()),
                ft.TextButton("نعم", on_click=lambda e: yes_click(e))
            ]
        )
        page.dialog.open = True
        page.update()

    show_login()

ft.app(target=main)
