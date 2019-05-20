import cmd
import pychromecast

import os, sys
from minio import Minio
from minio.error import ResponseError
import logging
import select
import time


minio_server = os.environ['MINIO_SERVER']
minio_access_key = os.environ['ACCESS_KEY']
minio_secret_key = os.environ['SECRET_KEY']
BUCKET_NAME = 'data'

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(nima.cast) '
    intro = "Welcome! Type ? to list commands"

    cast = None
    casts = None
    friendly_names = None
    fn = None

    minioClient = Minio(minio_server,
                    access_key= minio_access_key,
                    secret_key= minio_secret_key,
                    secure=False)

    def do_search(self, line):
        """Search a list of available devices..."""
        casts = pychromecast.get_chromecasts()
        if len(casts) == 0:
            print("No Devices Found")
        self.friendly_names = [cc.device.friendly_name for cc in casts]
        self.casts = casts
        for i in range(len(self.friendly_names)):
            fn = self.friendly_names[i]
            print('[{}] - {}'.format(i, fn))

    def do_select(self, num):
        """select [num] selects the number in the search results"""
        if not num:
            print("Please choose an index")
            return

        num = int(num)
        if num >= len(self.friendly_names):
            print("Index not in range, try again please")
            return

        self.fn = self.friendly_names[num]
        self.cast = self.casts[num]

        self.cast.connect()

    def do_device(self, line):
        """Shows the name of the selected device"""
        print(self.fn)
    
    def do_list(self, line):
        """List files on the server"""
        self.objects = list(self.minioClient.list_objects(BUCKET_NAME, prefix='tv/', recursive=True))
        i = 0
        for obj in self.objects:
            # print("[{}]- {}".format(i, self.minioClient.presigned_get_object(BUCKET_NAME, obj.object_name)))
            print("[{:2d}]- \t{}".format(i, obj.object_name))
            i += 1

    def do_play(self, num):
        """play [num] starts playing the file specified by the number in results of list"""
        if not num:
            print("Please choose an index, use <list> to list files")
            return

        num = int(num)
        if num >= len(self.objects):
            print("Index not in range, try again please")
            return

        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return

        obj = self.objects[num]
        url = self.minioClient.presigned_get_object(BUCKET_NAME, obj.object_name)
        print(url)

        # try:
        #     self.cast.media_controller.stop()
        # except:
        #     pass
        # self.cast.play_media(url, "video/mp4")

        t = 0
        while True:
            polltime = 0.1
            can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
            if can_read:
                #received something on the socket, handle it with run_once()
                self.cast.socket_client.run_once()

            t += 1
            if t == 5:
                self.cast.play_media(url, "video/mp4")

            if t > 10:
                break

            time.sleep(1)

    def do_seek(self, time):
        """seek [time] starts playing the file on the specified time"""
        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return
        time = int(time)
        self.cast.wait()
        mc = self.cast.media_controller
        mc.seek(time)


    def do_stream(self, url):
        """stream [url] starts playing the file specified by the url"""
        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return

        self.cast.wait()
        mc = self.cast.media_controller
        mc.play_media(url, 'video/mp4')
        mc.block_until_active(10)

        # t = 0
        # while True:
        #     polltime = 0.1
        #     can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
        #     if can_read:
        #         #received something on the socket, handle it with run_once()
        #         self.cast.socket_client.run_once()

        #     t += 1
        #     if t == 5:
        #         self.cast.play_media(url, "video/mp4")

        #     if t > 10:
        #         break

        #     time.sleep(1)
                

    def do_pause(self, line):
        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return
        
        t = 0
        while True:
            polltime = 0.1
            can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
            if can_read:
                #received something on the socket, handle it with run_once()
                self.cast.socket_client.run_once()

            t += 1
            if t > 5:
                self.cast.media_controller.pause()
                break

            time.sleep(1)
        
    def do_resume(self, line):
        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return
        
        t = 0
        while True:
            polltime = 0.1
            can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
            if can_read:
                #received something on the socket, handle it with run_once()
                self.cast.socket_client.run_once()

            t += 1
            if t > 5:
                self.cast.media_controller.play()
                break

            time.sleep(1)

    def do_stop(self, line):
        if not self.cast:
            print("please select cast device using <select>, use <search> for options")
            return

        t = 0
        while True:
            polltime = 0.1
            can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
            if can_read:
                #received something on the socket, handle it with run_once()
                self.cast.socket_client.run_once()

            t += 1
            if t > 5:
                self.cast.media_controller.stop()
                break

            time.sleep(1)

    
    def do_EOF(self, line):
        # t = 0
        # if self.cast:
        #     while True:
        #         polltime = 0.1
        #         can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
        #         if can_read:
        #             #received something on the socket, handle it with run_once()
        #             self.cast.socket_client.run_once()

        #         t += 1
        #         if t > 5:
        #             self.cast.quit_app()
        #             break

        #         time.sleep(1)

        return True

    def do_exit(self, line):
        # t = 0
        # if self.cast:
        #     while True:
        #         polltime = 0.1
        #         can_read, _, _ = select.select([self.cast.socket_client.get_socket()], [], [], polltime)
        #         if can_read:
        #             #received something on the socket, handle it with run_once()
        #             self.cast.socket_client.run_once()

        #         t += 1
        #         if t > 5:
        #             self.cast.quit_app()
        #             break

        #         time.sleep(1)
        return True

if '--show-debug' in sys.argv:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    HelloWorld().cmdloop()
