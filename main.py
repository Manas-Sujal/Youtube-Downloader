import flet as ft
from pathlib import Path
global downloads_path        
import os
from pytube import YouTube
from pytube import Channel
import urllib.request
import re
from sys import argv
import pafy
from bs4 import BeautifulSoup 
import requests
import json 
import threading
from moviepy.editor import *
from collections import OrderedDict
downloads_path = str(Path.home() / "Downloads")

def main(page: ft.Page):
    page.title = "Youtube Downloader - Manas Sujal"
    page.window_width=650
    page.window_height=500
    #page.scroll = ft.ScrollMode.ADAPTIVE
    # Enter URl and Download
    url_field = ft.TextField(hint_text="Enter Video URL", width=400, height = 75)
    status = ft.Text(text_align=ft.TextAlign.CENTER, size=17)
    
    def download_the_video_mp4_entered_url(e):
        def download_mp4_for_entered():
            try:
                status.color=ft.colors.WHITE
                status.value = f"Downloading..."
                page.update()
                link = url_field.value
                status.value = f"Downloading... 20%"
                page.update()
                yt = YouTube(link)
                status.value = f"Downloading...40%"
                page.update()
                yd = yt.streams.get_highest_resolution()
                status.value = f"Downloading...60%"
                page.update()
                yd.download(downloads_path)
                status.value = f"Downloading...80%"
                page.update()
                status.value = f"Downloaded ! "
                status.color=ft.colors.GREEN
                page.update()
            except :
                status.value = f"Can't Download ! "
                status.color=ft.colors.RED
                page.update()

        threading.Thread(target=download_mp4_for_entered).start()
    def download_the_video_mp3_entered_url(e):
        def download_mp3_for_entered():
            try:
                status.color=ft.colors.WHITE
                status.value = f"Downloading..."
                page.update()
                link = url_field.value
                yt = YouTube(link)
                status.value = f"Downloading... 10%"
                page.update()
                yd = yt.streams.filter(only_audio=True).first()
                status.value = f"Downloading... 20%"
                page.update()
                dest=downloads_path
                status.value = f"Downloading... 30%"
                page.update()
                outfile = yd.download(output_path=dest)
                status.value = f"Downloading... 40%"
                page.update()
                base = os.path.splitext(outfile)[0]
                status.value = f"Downloading... 50%"
                page.update()
                new_file = base+ '.mp3'
                status.value = f"Downloading... 60%"
                page.update()
                mp4_no_frame = AudioFileClip(outfile)
                status.value = f"Downloading... 70%"
                page.update()
                mp4_no_frame.write_audiofile(new_file, logger=None)
                status.value = f"Downloading... 80%"
                page.update()
                mp4_no_frame.close()
                status.value = f"Downloading... 90%"
                page.update()
                os.remove(outfile)
                status.value = f"Downloading... 100%"
                page.update()
                #os.rename(outfile, new_file)
                status.value = f"Downloaded ! "
                status.color=ft.colors.GREEN
                page.update()
            except:
                status.value = f"Can't Download ! "
                status.color=ft.colors.RED
                page.update()
        threading.Thread(target=download_mp3_for_entered).start()

    ## SEARCH AND DOWNLOAD
    styl=ft.TextStyle(size=14)
    search_field = ft.TextField(hint_text="Enter Video Search",hint_style=styl,label_style=styl, width=350, height = 40)
    number_result_field = ft.TextField(width= 150, height = 40)
    selected_row_text = ft.Text(text_align=ft.TextAlign.CENTER, size=15)
    status_search_dwnld = ft.Text(text_align=ft.TextAlign.CENTER, size=17)
    search_tree=ft.DataTable(
                                    #data_row_color={"selected": "yellow"},
                                columns=[
                                    ft.DataColumn(ft.Text("Title")),
                                    ft.DataColumn(ft.Text("Channel Name")),
                                    ft.DataColumn(ft.Text("Views")),
                                    ft.DataColumn(ft.Text("Video Code"), visible=False),
                                ],
                                rows=[],
                                )


    #download for searched
    def download_mp3_for_searched(video_id):
        def download_mp3_for_searched(id_video):
            try:
                status_search_dwnld.color=ft.colors.WHITE
                status_search_dwnld.value = f"Downloading..."
                page.update()
                link = "https://www.youtube.com/watch?v="+id_video
                yt = YouTube(link)
                status_search_dwnld.value = f"Downloading... 10%"
                page.update()
                yd = yt.streams.filter(only_audio=True).first()
                status_search_dwnld.value = f"Downloading... 20%"
                page.update()
                dest=downloads_path
                status_search_dwnld.value = f"Downloading... 30%"
                page.update()
                outfile = yd.download(output_path=dest)
                status_search_dwnld.value = f"Downloading... 40%"
                page.update()
                base = os.path.splitext(outfile)[0]
                status_search_dwnld.value = f"Downloading... 50%"
                page.update()
                new_file = base+ '.mp3'
                status_search_dwnld.value = f"Downloading... 60%"
                page.update()
                mp4_no_frame = AudioFileClip(outfile)
                status_search_dwnld.value = f"Downloading... 70%"
                page.update()
                mp4_no_frame.write_audiofile(new_file, logger=None)
                status_search_dwnld.value = f"Downloading... 80%"
                page.update()
                mp4_no_frame.close()
                status_search_dwnld.value = f"Downloading... 90%"
                page.update()
                os.remove(outfile)
                status.value = f"Downloading... 100%"
                page.update()
                status_search_dwnld.value = f"Downloaded ! "
                status_search_dwnld.color=ft.colors.GREEN
                page.update()
            except:
                status_search_dwnld.value = f"Can't Download ! "
                status_search_dwnld.color=ft.colors.RED
                page.update()
        threading.Thread(target=download_mp3_for_searched(video_id)).start()
        
    def download_mp4_for_searched(video_id):
        def download_mp4_for_searched(id_video):
            try:
                status_search_dwnld.color=ft.colors.WHITE
                status_search_dwnld.value = f"Downloading..."
                page.update()
                link = "https://www.youtube.com/watch?v="+id_video
                status_search_dwnld.value = f"Downloading... 20%"
                page.update()
                yt = YouTube(link)
                status_search_dwnld.value = f"Downloading...40%"
                page.update()
                yd = yt.streams.get_highest_resolution()
                status_search_dwnld.value = f"Downloading...60%"
                page.update()
                yd.download(downloads_path)
                status_search_dwnld.value = f"Downloading...80%"
                page.update()
                status_search_dwnld.value = f"Downloaded ! "
                status_search_dwnld.color=ft.colors.GREEN
                page.update()
            except :
                status_search_dwnld.value = f"Can't Download ! "
                status_search_dwnld.color=ft.colors.RED
                page.update()

        threading.Thread(target=download_mp4_for_searched(video_id)).start()
        
    dwmld_mp3_but = ft.OutlinedButton("Download MP3", width=300, disabled=True)
    dwmld_mp4_but = ft.OutlinedButton("Download MP4", width=300, disabled=True)
    def selected_from_search(video_search_download_id,video_selected_title, channel_name_selected):
        
        selected_row_text.value=f"Selected Video : {video_selected_title} | {channel_name_selected}"
        dwmld_mp3_but.disabled = False
        dwmld_mp3_but.on_click=lambda e:download_mp3_for_searched(video_search_download_id)
        dwmld_mp4_but.disabled = False
        dwmld_mp4_but.on_click=lambda e:download_mp4_for_searched(video_search_download_id)

        
    def search_yt(e):
        def search():
            dwmld_mp3_but.disabled = True
            dwmld_mp4_but.disabled = True
            selected_row_text.value=""
            status_search_dwnld.value=""
            for x in range(len(search_tree.rows)):
                del search_tree.rows[0]
            search_keyword = search_field.value
            if str(number_result_field.value) == '':
                no_of_results=10
            else:
                no_of_results= int(number_result_field.value)
            if ' ' in search_keyword:
                search_keyword = search_keyword.replace(' ','+')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+(search_keyword))
            video_ids_1= re.findall(r"watch\?v=(\S{11})", html.read().decode())
            #video_ids = list(set(video_ids))
            video_ids = []
            for item in video_ids_1:
              if item not in video_ids:
                video_ids.append(item)
            for z in range(no_of_results):
                link = ("https://www.youtube.com/watch?v="+video_ids[z])
                x=YouTube(link)
                curl = x.channel_url
                c=Channel(curl) 
                ChannelName = c.channel_name
                video_title=x.title
                video_views=x.views
                search_tree.width=750
                search_tree.rows.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(video_title)),
                            ft.DataCell(ft.Text(ChannelName)),
                            ft.DataCell(ft.Text(video_views)),
                            ft.DataCell(ft.Text(video_ids[z])),
                            ft.DataCell(ft.Text(z))
                            ],
                        on_select_changed = lambda e:selected_from_search(e.control.cells[3].content.value, e.control.cells[0].content.value,e.control.cells[1].content.value)
                        )
                    )
                    

        threading.Thread(target=search).start()
        
            
    
    t = ft.Tabs(                
                tab_alignment=ft.TabAlignment.CENTER,
                selected_index=0,
                
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        
                        text="Enter URL and Download",
                        content=
                            ft.Column(
                                width={page.width},
                                controls=[
                                    ft.Row(controls=[ft.Text("", height=15,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[ft.Text("Faster internet, faster online downloads.",size=10,text_align=ft.TextAlign.RIGHT)],alignment=ft.MainAxisAlignment.END),
                                    ft.Row(controls=[ft.Text("", height=15,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[ft.Text("Enter Link of Video:",text_align=ft.TextAlign.CENTER, size=17)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[ft.Text("", height=5,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[url_field],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[ft.Text("", height=5,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[
                                            ft.OutlinedButton(text="Download MP3", on_click=download_the_video_mp3_entered_url),
                                            ft.Row(controls=[ft.Text("", width=10,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                            ft.OutlinedButton("Download MP4", on_click=download_the_video_mp4_entered_url),
                                        ]
                                           ,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[ft.Text("", height=5,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row(controls=[status],alignment=ft.MainAxisAlignment.CENTER),
                                    
                                    ]
                                ),
                            
                        ),       
                        
                    ft.Tab(
                        text="Search and Download",
                        content=ft.Column(
                                width={page.width},
                                controls=[
    
                                        #ft.Row(controls=[ft.Text("", height=5,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Row(controls=[ft.Text("Faster internet, faster online searches and downloads.",size=10,text_align=ft.TextAlign.RIGHT)],alignment=ft.MainAxisAlignment.END),
                                       ft.Row(
                                           width={page.width},
                                           controls=[
                                            ft.Column(controls=[ft.Text("Search the Video:",width=350,text_align=ft.TextAlign.CENTER, size=17)]),
                                            ft.Column(controls=[ft.Text("Enter Number of Results:",width=150,text_align=ft.TextAlign.CENTER, size=17)]),
                                            ft.Column(controls=[ft.Text("",width=100,text_align=ft.TextAlign.CENTER, size=17)]),
                                        ]
                                            ,alignment=ft.MainAxisAlignment.CENTER
                                           ),
                                       ft.Row(
                                           width={page.width},
                                           controls=[
                                            ft.Column(controls=[search_field]),
                                            ft.Column(controls=[number_result_field]),
                                            ft.Column(controls=[ft.OutlinedButton("Search", width=100, on_click=search_yt)]),
                                        ]
                                           ,alignment=ft.MainAxisAlignment.CENTER
                                           ),
                                        ft.Row(controls=[ft.Text("", height=5,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                                
                                       ft.Row(
                                           controls=[ft.Column(height=240,scroll=ft.ScrollMode.ALWAYS,controls=[search_tree])],
                                           alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Row(controls=[ft.Text("", height=3,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Divider(),
                                        ft.Row(controls=[selected_row_text],alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Divider(),
                                        ft.Row(controls=[
                                            ft.Column(controls=[dwmld_mp3_but]),
                                            ft.Column(controls=[dwmld_mp4_but]),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Row(controls=[ft.Text("", height=3,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Row(controls=[status_search_dwnld],alignment=ft.MainAxisAlignment.CENTER),
                                        
                                        
                                        ])                                    
                                     
                                ),
                    
                ],
            )

    def check_switch():
        while True:
            if t.selected_index ==1:
                page.window_width=850
                page.window_height=800
                page.update()
            else:
                page.window_width=650
                page.window_height=500
                page.update()
            
    threading.Thread(target=check_switch).start()
    
    page.add(
        ft.Column(
            
            height={page.height},
            width={page.width},
            controls=[
                ft.Row(
                            [ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "Youtube Downloader",
                                        ft.TextStyle(
                                            size=30,
                                            weight=ft.FontWeight.BOLD,
                                            decoration=ft.TextDecoration.UNDERLINE
                                            
                                        ), ),],)],          
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                ft.Row(controls=[ft.Text("", height=10,text_align=ft.TextAlign.CENTER)],alignment=ft.MainAxisAlignment.CENTER),
                t
            ],

        )
   
    )
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
