from pytube import YouTube
import PySimpleGUI as sg

Link = [
    [sg.Text("Link of the Video"),
        sg.In(size=(50, 1), enable_events=True, key="Link")
    ],
        
    [sg.Text("Download Path"),
        sg.In("C:/", size=(50, 1), enable_events=True, key="Path", pad = (15,0)),
        sg.FolderBrowse("Open", size = (10, 1), initial_folder = "C:/")
    ]
]
Button = [
    [sg.Button(button_text = "Download", key = "DownloadButton", size = (10, 1))]
]
Output = [
    [sg.Text(key = "OutputText")]
]

layout = [
    [sg.Column(Link)],
    [sg.Column(Button, justification = "center")],
    [sg.Column(Output)]
]

window = sg.Window("Youtube Video Downloader", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "DownloadButton":
        link = values["Link"]
        print(link)
        window["OutputText"].update("Working...")
        window.refresh()
        try:
            yt = YouTube(link)  
            yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = values['Path'], filename = "{0}.mp4".format(yt.title))
            print('Task Completed!')
            window["OutputText"].update("Successfully downloaded the Video with the Title: {0}!".format(yt.title))
        except:
            print("Error! \n\tLink -> {0}\n\t Path -> {1}".format(values['Link'], values['Path']))
            window["OutputText"].update("Error!")

