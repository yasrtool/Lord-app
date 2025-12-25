import flet as ft

def main(page: ft.Page):
    # --- إعدادات الصفحة الاحترافية ---
    page.title = "English Stage 2 - Professional"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 800
    page.padding = 0
    page.spacing = 0
    page.fonts = {
        "Poppins": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Poppins")

    # --- [الميزة 2: إدارة المستخدمين] ---
    # يمكن لاحقاً ربط هذه القائمة بقاعدة بيانات أونلاين
    ADMIN_DATABASE = {
        "nour_admin": "2026",
        "student_user": "yasr_ammar",
        "ahmed_hilla": "yASR-AMAR1AA"
    }

    # --- [الميزة 3: المراسلة الحية] ---
    def contact_admin(e):
        # يفتح حسابك التليجرام مباشرة للمراسلة
        page.launch_url("https://t.me/Yasr_ammar1") # ضع يوزرك هنا

    # --- دالة الرجوع للرئيسية ---
    def go_home(e):
        show_dashboard()

    # --- [الميزة 4: صفحات المواد المنظمة] ---
    def show_subject_details(subject_name):
        page.clean()
        page.appbar = ft.AppBar(
            title=ft.Text(f"Subject: {subject_name}"),
            bgcolor=ft.colors.BLUE_GREY_900,
            color=ft.colors.WHITE,
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_home),
        )
        
        # محتوى تجريبي للمادة
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PICTURE_AS_PDF, color="red"),
                        title=ft.Text(f"Chapter 1 - {subject_name} Summary"),
                        subtitle=ft.Text("PDF File - 2.4 MB"),
                        trailing=ft.IconButton(ft.icons.DOWNLOAD),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PLAY_CIRCLE_FILL, color="blue"),
                        title=ft.Text("Video Lecture: Introduction"),
                        subtitle=ft.Text("YouTube Link"),
                        on_click=lambda _: page.launch_url("https://youtube.com")
                    ),
                ]),
                padding=20
            )
        ])
        page.add(content)
        page.update()

    # --- [الميزة 1: الواجهة الاحترافية - لوحة التحكم] ---
    def show_dashboard():
        page.clean()
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRADUATION_CAP, color=ft.colors.WHITE),
            title=ft.Text("English Stage 2", color=ft.colors.WHITE, weight="bold"),
            bgcolor=ft.colors.BLUE_700,
            center_title=True,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Live Support", 
                            icon=ft.icons.SUPPORT_AGENT, 
                            on_click=contact_admin
                        ),
                        ft.PopupMenuItem(
                            text="About App", 
                            icon=ft.icons.INFO_OUTLINE
                        ),
                        ft.PopupMenuItem(
                            text="Logout", 
                            icon=ft.icons.LOGOUT,
                            on_click=lambda _: main(page) # إعادة تشغيل التطبيق (تسجيل خروج)
                        ),
                    ]
                )
            ]
        )

        # بطاقات المواد بتصميم عصري
        subjects = [
            ("Phonetics", "الصوت", ft.icons.SENSORS, ft.colors.AMBER_700),
            ("Grammar", "القواعد", ft.icons.STAIRS, ft.colors.GREEN_700),
            ("Drama", "الدراما", ft.icons.THEATER_COMEDY, ft.colors.PURPLE_700),
            ("Short Story", "القصص القصيرة", ft.icons.AUTO_STORIES, ft.colors.RED_700),
            ("writing", "الإنشاء", ft.icons.EDIT_NOTE, ft.colors.BLUE_700),
            ("Speaking", "سبيكنك", ft.icons.HEADSET, ft.colors.CYAN_700),
        ]

        grid = ft.GridView(
            expand=1,
            runs_count=2,
            max_extent=200,
            child_aspect_ratio=1.0,
            spacing=15,
            run_spacing=15,
            padding=20,
        )

        for eng, arb, icon, color in subjects:
            grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(icon, size=45, color=color),
                        ft.Text(eng, size=16, weight="bold", color=ft.colors.BLUE_GREY_900),
                        ft.Text(arb, size=12, color=ft.colors.BLUE_GREY_400),
                    ], alignment="center", horizontal_alignment="center"),
                    bgcolor=ft.colors.WHITE,
                    border_radius=20,
                    shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(0.1, "black")),
                    on_click=lambda e, name=eng: show_subject_details(name), # الانتقال لصفحة المادة
                )
            )

        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Welcome Back, Student!", size=22, weight="bold"),
                    ft.Text("Choose your subject to start studying", size=14, color="grey"),
                    ft.Divider(height=20, color="transparent"),
                    grid
                ]),
                padding=20,
                expand=True
            )
        )
        page.update()

    # --- واجهة تسجيل الدخول ---
    def login_screen():
        user_field = ft.TextField(
            label="Admin Username", 
            prefix_icon=ft.icons.PERSON,
            border_radius=15,
            width=300
        )
        pass_field = ft.TextField(
            label="Access Code", 
            prefix_icon=ft.icons.LOCK,
            password=True, 
            can_reveal_password=True,
            border_radius=15,
            width=300
        )

        def attempt_login(e):
            if user_field.value in ADMIN_DATABASE and ADMIN_DATABASE[user_field.value] == pass_field.value:
                show_dashboard()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Invalid Access Credentials! Contact Nour."))
                page.snack_bar.open = True
                page.update()

        login_view = ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.LOCK_PERSON, size=80, color=ft.colors.BLUE_700),
                ft.Text("Student Portal Login", size=24, weight="bold"),
                ft.Text("Enter the credentials provided by your Admin", size=13, color="grey"),
                ft.Divider(height=20, color="transparent"),
                user_field,
                pass_field,
                ft.Divider(height=10, color="transparent"),
                ft.ElevatedButton(
                    "Authorize & Enter",
                    on_click=attempt_login,
                    width=300,
                    height=50,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_700,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=15)
                    )
                ),
            ], horizontal_alignment="center", alignment="center"),
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.BLUE_50, ft.colors.WHITE]
            )
        )
        page.add(login_view)

    login_screen()

# لتشغيل التطبيق
ft.app(target=main)
