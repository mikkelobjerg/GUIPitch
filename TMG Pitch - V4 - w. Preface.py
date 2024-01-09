import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import vlc
import webbrowser


#---------------------------------------Log in function-----------------------------------#

def login(event=None):
    valid_credentials = {
        "MBJ": "BDYEuf8/n4PE",
        "NT": "BDYEuf8/n4PE",
        "DS": "BDYEuf8/n4PE",
        "JK": "BDYEuf8/n4PE",
        "MA": "BDYEuf8/n4PE",
        "PW": "BDYEuf8/n4PE",
    }
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # -----------------------------------Preface login-------------------------------------#

    if entered_username in valid_credentials and valid_credentials[entered_username] == entered_password:
        print("Successfully logged in")
        window.destroy()
        TMG_preface = tk.Tk()
        TMG_preface.title("THE MARKETING GUY")

        # Function to toggle full screen
        def toggle_fullscreen1(event=None):
            TMG_preface.attributes('-fullscreen', not TMG_preface.attributes('-fullscreen'))
        # Bind the escape key to toggle full screen
        TMG_preface.bind('<Escape>', toggle_fullscreen1)
        # Set the window to full screen
        TMG_preface.attributes('-fullscreen', True)
        TMG_preface.iconbitmap('images/icon.ico')
        TMG_preface.state("zoomed")


        screen_width = TMG_preface.winfo_screenwidth()  # Get the width of the screen
        screen_height = TMG_preface.winfo_screenheight()  # Get the height of the screen

        # Calculate center coordinates
        center_x = screen_width / 2
        center_y = screen_height / 2

        bg_image_preface = PhotoImage(file="images/logowall.png")
        canvas_preface = tk.Canvas(TMG_preface, width=640, height=840)

        # White background to fill out empty space from logowall
        canvas_image_bg = PhotoImage(file="images/white_bg.png")
        white_bg = canvas_preface.create_image(755, 570, image=canvas_image_bg)  # Placing the image on board


        canvas_preface.pack(fill="both", expand=True)
        preface_image = canvas_preface.create_image(center_x, center_y, image=bg_image_preface, anchor="center")

        def update_preface_image_position(event=None):
            # Recalculate center coordinates
            new_center_x = TMG_preface.winfo_width() / 2
            new_center_y = TMG_preface.winfo_height() / 2

            # Move the image to the new center
            canvas_preface.coords(preface_image, new_center_x, new_center_y)

        # Bind the update function to window resize event
        TMG_preface.bind("<Configure>", update_preface_image_position)




        # ----------------------------------- TMG Dashboard -------------------------------------#

        def validering(event=None):
            TMG_preface.destroy()
            TMG_window = tk.Tk()
            TMG_window.title("TMG Dashboard")

            # Function to toggle full screen
            def toggle_fullscreen(event=None):
                TMG_window.attributes('-fullscreen', not TMG_window.attributes('-fullscreen'))
            # Bind the escape key to toggle full screen
            TMG_window.bind('<Escape>', toggle_fullscreen)
            # Set the window to full screen
            TMG_window.attributes('-fullscreen', True)
            TMG_window.iconbitmap('images/icon.ico')
            TMG_window.state("zoomed")


            bg_image_dashboard = PhotoImage(file="images/background.png")
            TMG_canvas = tk.Canvas(TMG_window, width=1500, height=800)
            TMG_canvas.pack(fill="both", expand=True)
            TMG_canvas.create_image(750, 400, image=bg_image_dashboard, anchor="center")

            TMG_canvas.create_text(
                750, 65
                ,
                text=" ",
                fill="#000000",
                font=("Khand", int(40.0)))


            # -------------------Images on TMG Dashboard--------------------------#

            # Find Screen dimensions
            screen_width = TMG_window.winfo_screenwidth()  # Get the width of the screen
            screen_height = TMG_window.winfo_screenheight()  # Get the height of the screen

            # Calculate center coordinates
            center_x = screen_width / 2
            center_y = screen_height / 2


            TMG_Bjerg = PhotoImage(file="images/bjerg.png")
            Bjerg_image = TMG_canvas.create_image(center_x, center_y, image=TMG_Bjerg)  # Placing the image in the center


            # Rapport-billede
            TMG_Rapport_Test = PhotoImage(file="images/rapport.png")
            rapport_image = TMG_canvas.create_image(88, 295, image=TMG_Rapport_Test)
            TMG_Rapport_Highlighted = PhotoImage(file="images/rapport_highlighted.png")  # Replaced with highlighted image

            TMG_Ad1 = PhotoImage(file="images/Ad1.png")  # Load Ad1-billede
            Ad1_image = TMG_canvas.create_image(1020, 420, image=TMG_Ad1)  # Placing the image on board
            Ad1_Highlighted = PhotoImage(file="images/Ad1_Highlighted.png")  # Replaced with highlighted image

            TMG_Ad2 = PhotoImage(file="images/Ad2.png")
            Ad2_image = TMG_canvas.create_image(1065, 439, image=TMG_Ad2)  # Placing the image on board
            Ad2_Highlighted = PhotoImage(file="images/Ad2_Highlighted.png")  # Replaced with highlighted image

            TMG_Ad3 = PhotoImage(file="images/Ad3.png")
            Ad3_image = TMG_canvas.create_image(1111, 460, image=TMG_Ad3)  # Placing the image on board
            Ad3_Highlighted = PhotoImage(file="images/Ad3_Highlighted.png")  # Replaced with highlighted image

            TMG_Ad4 = PhotoImage(file="images/Ad4.png")
            Ad4_image = TMG_canvas.create_image(976, 440, image=TMG_Ad4)  # Placing the image on board
            Ad4_Highlighted = PhotoImage(file="images/Ad4_Highlighted.png")  # Replaced with highlighted image

            TMG_Ad5 = PhotoImage(file="images/Ad5.png")
            Ad5_image = TMG_canvas.create_image(1024, 462, image=TMG_Ad5)  # Placing the image on board
            Ad5_Highlighted = PhotoImage(file="images/Ad5_Highlighted.png")  # Replaced with highlighted image

            TMG_Ad6 = PhotoImage(file="images/Ad6.png")
            Ad6_image = TMG_canvas.create_image(1072, 482, image=TMG_Ad6)  # Placing the image on board
            Ad6_Highlighted = PhotoImage(file="images/Ad6_Highlighted.png")  # Replaced with highlighted image


            TMG_Target1 = PhotoImage(file="images/target01.png")
            Target1_image = TMG_canvas.create_image(800, 550, image=TMG_Target1)  # Placing the image on board
            Target1_Highlighted = PhotoImage(file="images/target01_HL.png")  # Replaced with highlighted image

            TMG_Target2 = PhotoImage(file="images/target02.png")
            Target2_image = TMG_canvas.create_image(867, 575, image=TMG_Target2)  # Placing the image on board
            Target2_Highlighted = PhotoImage(file="images/target02_HL.png")  # Replaced with highlighted image

            TMG_Target3 = PhotoImage(file="images/target03.png")
            Target3_image = TMG_canvas.create_image(755, 570, image=TMG_Target3)  # Placing the image on board
            Target3_Highlighted = PhotoImage(file="images/target03_HL.png")  # Replaced with highlighted image

            TMG_Target4 = PhotoImage(file="images/target04.png")
            Target4_image = TMG_canvas.create_image(830, 626, image=TMG_Target4)  # Placing the image on board
            Target4_Highlighted = PhotoImage(file="images/target04_HL.png")  # Replaced with highlighted image

            TMG_Target5 = PhotoImage(file="images/target05.png")
            Target5_image = TMG_canvas.create_image(762, 317, image=TMG_Target5)  # Placing the image on board
            Target5_Highlighted = PhotoImage(file="images/target05_HL.png")  # Replaced with highlighted image


            # Defining hoover functions
            def on_enter(event):
                TMG_canvas.itemconfig(rapport_image, image=TMG_Rapport_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave(event):
                TMG_canvas.itemconfig(rapport_image, image=TMG_Rapport_Test)
                TMG_canvas.config(cursor="arrow")

            def on_enter_1(event):
                TMG_canvas.itemconfig(Ad1_image, image=Ad1_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_1 (event):
                TMG_canvas.itemconfig(Ad1_image, image=TMG_Ad1)
                TMG_canvas.config(cursor="arrow")

            def on_enter_2(event):
                TMG_canvas.itemconfig(Ad2_image, image=Ad2_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_2 (event):
                TMG_canvas.itemconfig(Ad2_image, image=TMG_Ad2)
                TMG_canvas.config(cursor="arrow")

            def on_enter_3(event):
                TMG_canvas.itemconfig(Ad3_image, image=Ad3_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_3 (event):
                TMG_canvas.itemconfig(Ad3_image, image=TMG_Ad3)
                TMG_canvas.config(cursor="arrow")

            def on_enter_4(event):
                TMG_canvas.itemconfig(Ad4_image, image=Ad4_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_4 (event):
                TMG_canvas.itemconfig(Ad4_image, image=TMG_Ad4)
                TMG_canvas.config(cursor="arrow")

            def on_enter_5(event):
                TMG_canvas.itemconfig(Ad5_image, image=Ad5_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_5 (event):
                TMG_canvas.itemconfig(Ad5_image, image=TMG_Ad5)
                TMG_canvas.config(cursor="arrow")

            def on_enter_6(event):
                TMG_canvas.itemconfig(Ad6_image, image=Ad6_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_6 (event):
                TMG_canvas.itemconfig(Ad6_image, image=TMG_Ad6)
                TMG_canvas.config(cursor="arrow")

            def on_enter_7(event):
                TMG_canvas.itemconfig(Target1_image, image=Target1_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_7 (event):
                TMG_canvas.itemconfig(Target1_image, image=TMG_Target1)
                TMG_canvas.config(cursor="arrow")

            def on_enter_8(event):
                TMG_canvas.itemconfig(Target2_image, image=Target2_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_8 (event):
                TMG_canvas.itemconfig(Target2_image, image=TMG_Target2)
                TMG_canvas.config(cursor="arrow")

            def on_enter_9(event):
                TMG_canvas.itemconfig(Target3_image, image=Target3_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_9 (event):
                TMG_canvas.itemconfig(Target3_image, image=TMG_Target3)
                TMG_canvas.config(cursor="arrow")

            def on_enter_10(event):
                TMG_canvas.itemconfig(Target4_image, image=Target4_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_10 (event):
                TMG_canvas.itemconfig(Target4_image, image=TMG_Target4)
                TMG_canvas.config(cursor="arrow")

            def on_enter_11(event):
                TMG_canvas.itemconfig(Target5_image, image=Target5_Highlighted)
                TMG_canvas.config(cursor="hand2")

            def on_leave_11 (event):
                TMG_canvas.itemconfig(Target5_image, image=TMG_Target5)
                TMG_canvas.config(cursor="arrow")


            # Binding the hover events
            TMG_canvas.tag_bind(rapport_image, "<Enter>", on_enter)
            TMG_canvas.tag_bind(rapport_image, "<Leave>", on_leave)
            TMG_canvas.tag_bind(Ad1_image, "<Enter>", on_enter_1)
            TMG_canvas.tag_bind(Ad1_image, "<Leave>", on_leave_1)
            TMG_canvas.tag_bind(Ad2_image, "<Enter>", on_enter_2)
            TMG_canvas.tag_bind(Ad2_image, "<Leave>", on_leave_2)
            TMG_canvas.tag_bind(Ad3_image, "<Enter>", on_enter_3)
            TMG_canvas.tag_bind(Ad3_image, "<Leave>", on_leave_3)
            TMG_canvas.tag_bind(Ad4_image, "<Enter>", on_enter_4)
            TMG_canvas.tag_bind(Ad4_image, "<Leave>", on_leave_4)
            TMG_canvas.tag_bind(Ad5_image, "<Enter>", on_enter_5)
            TMG_canvas.tag_bind(Ad5_image, "<Leave>", on_leave_5)
            TMG_canvas.tag_bind(Ad6_image, "<Enter>", on_enter_6)
            TMG_canvas.tag_bind(Ad6_image, "<Leave>", on_leave_6)
            TMG_canvas.tag_bind(Target1_image, "<Enter>", on_enter_7)
            TMG_canvas.tag_bind(Target1_image, "<Leave>", on_leave_7)
            TMG_canvas.tag_bind(Target2_image, "<Enter>", on_enter_8)
            TMG_canvas.tag_bind(Target2_image, "<Leave>", on_leave_8)
            TMG_canvas.tag_bind(Target3_image, "<Enter>", on_enter_9)
            TMG_canvas.tag_bind(Target3_image, "<Leave>", on_leave_9)
            TMG_canvas.tag_bind(Target4_image, "<Enter>", on_enter_10)
            TMG_canvas.tag_bind(Target4_image, "<Leave>", on_leave_10)
            TMG_canvas.tag_bind(Target5_image, "<Enter>", on_enter_11)
            TMG_canvas.tag_bind(Target5_image, "<Leave>", on_leave_11)

            # Define initial offsets after creating the images
            initial_offsets = {
                rapport_image: (1083 - center_x, 358 - center_y),
                Ad1_image: (1187 - center_x, 574 - center_y),
                Ad2_image: (1234 - center_x, 593 - center_y),
                Ad3_image: (1280 - center_x, 613 - center_y),
                Ad4_image: (1146 - center_x, 592 - center_y),
                Ad5_image: (1193 - center_x, 613 - center_y),
                Ad6_image: (1240 - center_x, 634 - center_y),
                Target1_image: (974 - center_x, 701 - center_y),
                Target2_image: (1040 - center_x, 721 - center_y),
                Target3_image: (926 - center_x, 718 - center_y),
                Target4_image: (997 - center_x, 775 - center_y),
                Target5_image: (930 - center_x, 475 - center_y)
            }

            def update_image_position(event=None):
                # Recalculate center coordinates
                new_center_x = TMG_window.winfo_width() / 2
                new_center_y = TMG_window.winfo_height() / 2

                # Move Bjerg_image to the new center
                TMG_canvas.coords(Bjerg_image, new_center_x, new_center_y)

                # Update positions of all other images based on their offsets
                for img, offset in initial_offsets.items():
                    new_x = new_center_x + offset[0]
                    new_y = new_center_y + offset[1]
                    TMG_canvas.coords(img, new_x, new_y)

            # Bind the update function to window resize event
            TMG_window.bind("<Configure>", update_image_position)



            #Logo Button on page
            def logowall():
                TMG_logowall = tk.Toplevel()
                TMG_logowall.title("THE MARKETING GUY")
                TMG_logowall.geometry("1500x800")
                TMG_logowall.iconbitmap('images/icon.ico')
                TMG_logowall.state("zoomed")

                TMG_logowall.bg_image_logowall = PhotoImage(file="images/4.png") #this ensures, that the image is not garbage collected. For the future.
                canvas_logowall = tk.Canvas(TMG_logowall, width=640, height=840)
                canvas_logowall.pack(fill="both", expand=True)
                canvas_logowall.create_image(0, 0, image=TMG_logowall.bg_image_logowall, anchor="nw")

                # canvas_logowall.create_text(
                    # 750, 65,
                    # text="THE MARKETING GUY BLUEPRINT",
                    # fill="#000000",
                    # font=("Khand", int(40.0)))



            #--------------------image as button - Efter validering-button----------------------#
            # Load the image for the canvas
            canvas_image = PhotoImage(file="images/Button_Efter_validering.png")
            canvas_image_highlighted = PhotoImage(file="images/Button_Efter_validering_Highlight.png")
            # Place the image directly on the canvas
            image_on_canvas = TMG_canvas.create_image(1370, 480, image=canvas_image, anchor="center")
            # Bind a click event to the canvas image
            def on_canvas_click(event):
                logowall()
            TMG_canvas.tag_bind(image_on_canvas, "<Button-1>", on_canvas_click)

            def on_enter(event):
                TMG_canvas.itemconfig(image_on_canvas, image=canvas_image_highlighted)
                TMG_canvas.config(cursor="hand2")
            def on_leave(event):
                TMG_canvas.itemconfig(image_on_canvas, image=canvas_image)
                TMG_canvas.config(cursor="arrow")


            TMG_canvas.tag_bind(image_on_canvas, "<Enter>", on_enter)
            TMG_canvas.tag_bind(image_on_canvas, "<Leave>", on_leave)


            # -----------------Open PDF when clicked-----------------#
            def open_pdf(event=None):
                pdf_path = "G:/Shared drives/5. Pitch/PDF/Anonymiseret rapport.pdf"
                formatted_path = pdf_path.replace("\\", "/").replace(" ", "%20")
                url = f"file:///{formatted_path}"
                webbrowser.open(url)

            TMG_canvas.tag_bind(rapport_image, "<Button-1>", open_pdf)

            # ---------------- Play video on click function ----------------#
            def play_video(video_file):
                video_window = tk.Toplevel(TMG_window)
                video_window.title("TMG Media Player")
                video_window.iconbitmap('images/icon.ico')

                # Window size when opening
                base_width = 400
                width = base_width
                height = int(base_width * (5 / 4))  # 4:5 ratio
                video_window.geometry(f"{width}x{height}")

                # --------------VLC Settings-------------#
                # Create an instance of the VLC player
                Instance = vlc.Instance()
                player = Instance.media_player_new()

                # Create a new Frame in the Toplevel window to embed the video
                video_frame = tk.Frame(video_window, background="black")
                video_frame.pack(fill=tk.BOTH, expand=True)

                # Get the window ID of the frame for Windows
                video_window.update_idletasks()
                win_id = video_frame.winfo_id()
                player.set_hwnd(win_id)

                # Set media to VLC player
                Media = Instance.media_new(video_file)
                Media.get_mrl()
                player.set_media(Media)

                # Control buttons
                controls_frame = tk.Frame(video_window)
                controls_frame.pack(fill=tk.X)

                play_button = tk.Button(controls_frame, text="Play", font="Khand", command=lambda: player.play())
                pause_button = tk.Button(controls_frame, text="Pause", font="Khand", command=lambda: player.pause())
                stop_button = tk.Button(controls_frame, text="Stop", font="Khand", command=lambda: player.stop())

                play_button.pack(side=tk.LEFT)
                pause_button.pack(side=tk.LEFT)
                stop_button.pack(side=tk.LEFT)

                # Play the video
                player.play()

                # Bind the close window event
                video_window.protocol("WM_DELETE_WINDOW", lambda: on_video_window_close(player, video_window))

            def on_click(event, video_file):
                play_video(video_file)

            def on_video_window_close(player, video_window):
                player.stop()  # Stop the player
                player.release()  # Release the player resources
                video_window.destroy()  # Close the window

            TMG_canvas.tag_bind(Ad1_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad1.mp4"))
            TMG_canvas.tag_bind(Ad2_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad2.mp4"))
            TMG_canvas.tag_bind(Ad3_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad3.mp4"))
            TMG_canvas.tag_bind(Ad4_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad4.mp4"))
            TMG_canvas.tag_bind(Ad5_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad5.mp4"))
            TMG_canvas.tag_bind(Ad6_image, "<Button-1>", lambda event: on_click(event, "G:/Shared drives/5. Pitch/ad_videos/Ad6.mp4"))


            TMG_window.mainloop()


        # --------------- TMG Preface Button ------------------- #
        # Load the image for the canvas
        canvas_image_1 = PhotoImage(file="images/1.png")
        canvas_image_highlighted_1 = PhotoImage(file="images/2.png")


        # ----------- TMG Preface Button moves according to screen resize --------- #
        offset_x = 400  # Adjust this value as needed
        offset_y = -320  # Adjust this value as needed

        # Calculate initial center coordinates
        initial_center_x = TMG_preface.winfo_screenwidth() / 2
        initial_center_y = TMG_preface.winfo_screenheight() / 2

        # Place the image directly on the canvas with initial offsets
        image_on_canvas_1 = canvas_preface.create_image(initial_center_x + offset_x, initial_center_y + offset_y,
                                                        image=canvas_image_1, anchor="center")


        def update_preface_image_position(event=None):
            # Recalculate center coordinates
            new_center_x = TMG_preface.winfo_width() / 2
            new_center_y = TMG_preface.winfo_height() / 2
            # Move the background image to the new center
            canvas_preface.coords(preface_image, new_center_x, new_center_y)
            # Update the position of image_on_canvas_1 with the offset
            canvas_preface.coords(image_on_canvas_1, new_center_x + offset_x, new_center_y + offset_y)
        # Bind the update function to window resize event
        TMG_preface.bind("<Configure>", update_preface_image_position)




        # Bind a click event to the canvas image and the cursor hand
        def on_canvas_click_1(event):
            validering()
        canvas_preface.tag_bind(image_on_canvas_1, "<Button-1>", on_canvas_click_1)

        def on_enter2(event):
            canvas_preface.itemconfig(image_on_canvas_1, image=canvas_image_highlighted_1)
            canvas_preface.config(cursor="hand2")
        def on_leave2(event):
            canvas_preface.itemconfig(image_on_canvas_1, image=canvas_image_1)
            canvas_preface.config(cursor="arrow")

        canvas_preface.tag_bind(image_on_canvas_1, "<Enter>", on_enter2)
        canvas_preface.tag_bind(image_on_canvas_1, "<Leave>", on_leave2)


        TMG_preface.mainloop()
    else:
        messagebox.showerror(title="TMG Login Error", message="Incorrect Credentials for TMG Board")
        # error = tk.Tk()
        # error.geometry("500x250")
        #  error.iconbitmap('images/icon.ico')
        # ------Button-------#
        # def close_error():
         #   error.destroy()
        # close_button = tk.Button(error, text="TILBAGE", command=close_error, font="khand")
        # close_button.pack(expand=True)
        # error.mainloop()



# ---------------------------------- TMG Login ------------------------------------- #

# ----- Function to open up start window in the center ----- #
def center_window(win, width=640, height=740):
    # Get the screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    # Calculate x and y coordinates
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2.2) - (height / 2))
    win.geometry(f'{width}x{height}+{x}+{y}')


window = tk.Tk()
window.title("TMG Login")
window.geometry("0x0") # For at ikke se et vindue i starten der rykker sig
window.resizable(False, False)
window.iconbitmap("images/icon.ico")
# Center the window
center_window(window)


bg_image = PhotoImage(file="images/Baggrund PP - Mikkel.png")
canvas = tk.Canvas(window, width=640, height=840)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")

login_button = tk.Button(window, text="Login til TMG Dashboard", font="Khand", command=login)

def create_widget_on_canvas(widget, x, y):
    canvas.create_window(x, y, window=widget)

create_widget_on_canvas(username_entry, 370, 220)
create_widget_on_canvas(password_entry, 370, 280)
create_widget_on_canvas(login_button, 320, 380)

canvas.create_text(320, 100, text="THE MARKETING GUY", fill="#FFFFFF", font=("Khand", int(50.0)))
canvas.create_text(230, 220, text="Username:", fill="#999999", font=("Khand", int(24.0)))
canvas.create_text(230, 280, text="Password:", fill="#999999", font=("Khand", int(24.0)))

window.bind('<Return>', login)

window.mainloop()
