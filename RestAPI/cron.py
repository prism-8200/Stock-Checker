from RestAPI.DownloadZip import download_Parse


def cronjob():
    print('inside cron job')
    download_Parse()