JAZZMIN_SETTINGS = {
    # "related_modal_active": True,
    # "show_ui_builder": True,
    "site_title": "Zeynep",
    "site_header": "Admin Panel",
    "site_brand": "Zeynep",
    "custom_css": "main.css",
    # "show_sidebar": True,
    "navigation_expanded": False,  # Yon panelni avtomatik ochilmaslikka sozlash
    # `auth` ilovasini chap menyuda tartib bilan qo‘shish
    "order_with_respect_to": ["auth", "auth.User", "auth.Group"],

    # Ikonkalar qo‘shish
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
}