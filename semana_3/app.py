import web

urls = (
    '/(.*)', 'model.controller.cookies.Cookies'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()