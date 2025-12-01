# import libraries and modules
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# start tkinter to create the GUI window
root = Tk()
# set window size and position (width x height + x + y)
root.geometry("516x700+340+10")
# set player window title
root.title("Audio Player")
# set background color of the player
root.config(bg='#0f0f0f')
# prevent the user from resizing the window
root.resizable(False, False)
# initialize the mixer module
mixer.init()

# define function to add music from a selected folder
def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        # load only .mp3 files from the selected folder into the playlist
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

# define function to play the selected track from the playlist
def playMusic():
    music_name = Playlist.get(ACTIVE)
    # print the name without the .mp3 extension for debugging/info
    print(music_name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# add a frame for interface elements
lower_frm = Frame(root, bg="#000000", width=516, height=200)
lower_frm.place(x=0, y=0)

# number of frames in the GIF animation
frmcount = 32
# path to the GIF file (assumed to be in the same folder as this script)
# create a list of PhotoImage frames from the animation.gif
try:
    frms = [PhotoImage(file=os.path.join(os.path.dirname(__file__), 'animation.gif'), format='gif -index %i' % i) for i in range(frmcount)]
except Exception:
    # if GIF is missing or cannot be loaded, create an empty list to avoid crashes
    frms = []

# define function to update the GIF animation (if available)
def update(ind):
    if not frms:
        return
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

# place the GIF in the GUI
lbl = Label(root)
lbl.place(x=0, y=0)
# start animation if frames loaded
if frms:
    root.after(0, update, 0)

# add menu image (menu.png must be in the same folder)
try:
    menu = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'menu.png'))
    lb_menu = Label(root, image=menu, width=516, height=120)
    lb_menu.place(x=0, y=580)
except Exception:
    # fallback: a simple colored label if image is missing
    lb_menu = Label(root, bg="#111111", width=516, height=7)
    lb_menu.place(x=0, y=580)

# add a frame for the music controls and playlist
frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

# load button images (play/stop/pause). They should be in same folder.
try:
    btn_play = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'play.png'))
    btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=playMusic)
    btn_p.place(x=225, y=516)
except Exception:
    btn_p = Button(root, text="Play", bg='#0f0f0f', fg="#FFFFFF", command=playMusic)
    btn_p.place(x=225, y=516)

try:
    btn_stop = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'stop.png'))
    btn_s = Button(root, image=btn_stop, bg='#0f0f0f', height=50, width=50, command=mixer.music.stop)
    btn_s.place(x=140, y=516)
except Exception:
    btn_s = Button(root, text="Stop", bg='#0f0f0f', fg="#FFFFFF", command=mixer.music.stop)
    btn_s.place(x=140, y=516)

try:
    btn_pause = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'pause.png'))
    btn_ps = Button(root, image=btn_pause, bg='#0f0f0f', height=50, width=50, command=mixer.music.pause)
    btn_ps.place(x=310, y=516)
except Exception:
    btn_ps = Button(root, text="Pause", bg='#0f0f0f', fg="#FFFFFF", command=mixer.music.pause)
    btn_ps.place(x=310, y=516)

# add a button to choose a folder with music
btn_browse = Button(root, text="Choose Music Folder", font=('Arial', 15, 'bold'), fg="black", bg="#FFFFFF", width=48, command=addMusic)
btn_browse.place(x=0, y=572)

# configure playlist display with a scrollbar
Scroll = Scrollbar(frm_music)
Playlist = Listbox(
    frm_music,
    width=100,
    font=('Arial', 15, 'bold'),
    bg='#0f0f0f',
    fg='#00ff00',
    selectbackground="lightblue",
    cursor="hand2",
    bd=0,
    yscrollcommand=Scroll.set
)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# run the player window
root.mainloop()
