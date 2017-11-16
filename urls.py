import views


urlpatterns = [
        (r"/", views.MainHandler),
        (r"/delete", views.DeleteHandler),
        (r"/<order_id>", views.OrderHandler)
    ]

