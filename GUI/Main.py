import customtkinter as ctk

def main():
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("system")

    app = ctk.CTk()
    app.title("camera")
    app.geometry("600x400")
    app.minsize(width=600,height=400)

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=0)
    app.grid_rowconfigure(0, weight=1)

    video_frame = ctk.CTkFrame(
        master=app,
        fg_color="gray",
        border_width=2,
        border_color="black",
    )

    UI_frame = ctk.CTkFrame(
        master=app,
        fg_color="gray",
        border_width=2,
        border_color="black",
        width=120,
    )

    capture_button = ctk.CTkButton(
        master=UI_frame,
        width=100,
        height=100,
        text="capture",
        fg_color="blue",
        border_width=2,
        border_color="black",
    )
    record_button = ctk.CTkButton(
        master=UI_frame,
        width=100,
        height=100,
        text="capture",
        fg_color="blue",
        border_width=2,
        border_color="black",
    )
    gallery_button = ctk.CTkButton(
        master=UI_frame,
        width=100,
        height=100,
        text="gellery",
        fg_color="blue",
        border_width=2,
        border_color="black",
    )

    capture_button.place(
        x=10,
        rely=0.2
    )
    record_button.place(
        x=10,
        rely=0.4
    )
    gallery_button.place(
        x=10,
        rely=0.6
    )


    video_frame.grid(
        row=0,
        column=0,
        sticky="nsew",
    )

    UI_frame.grid(
        row=0,
        column=1,
        sticky="ns",
    )

    UI_frame.grid_propagate(False)


    app.mainloop()


    


if __name__ == "__main__" :
    main()