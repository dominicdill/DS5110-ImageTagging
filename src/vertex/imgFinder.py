newclasses = ["High School", "Skyline", "Police", "Busing", "Court",
          "arrest", "Protest", "housing", "Fire"  ]

from google_images_search import GoogleImagesSearch


DK=#
CX =#


def my_progressbar(url,progress):
    print(url + " " +progress + "%")


gis = GoogleImagesSearch(DK, CX, progressbar_fn=my_progressbar)
for i in newclasses:
    count=0
    with GoogleImagesSearch(DK, CX) as gis:
        _search_params = {
            'q': i,#df["Number"][0],
            'num': 10,
            'fileType': "png",
            'safe': 'off' ##
        }
        count=count+1
        gis.search(search_params=_search_params, path_to_dir=f"/src/classess/{i}",  custom_image_name=f"{i}_{count}")


