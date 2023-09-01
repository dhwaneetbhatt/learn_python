def show_args(title, *args, **kwargs):
    print(f"{title} args '{args}' and kwargs '{kwargs}'")

show_args("nothing")
show_args("one unnamed arg", 1)
show_args("one named arg", second="2")
show_args("two of each", 3, fourth="4")
