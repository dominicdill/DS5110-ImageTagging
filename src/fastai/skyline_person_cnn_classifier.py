from fastbook import *
from fastai.vision.widgets import *


path = Path('image_class')
image_classes = "city skyline", "person"


if not path.exists():
    path.mkdir()
    for o in image_classes:
        dest = (path/o)
        dest.mkdir(exist_ok=True)
        results = search_images_ddg(f"{o}")
        download_images(dest, urls=results)


failed = verify_images(fns)


failed.map(Path.unlink)


skylines_datablock = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))


skylines_datablock = skylines_datablock.new(
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms())
dls = skylines_datablock.dataloaders(path)


learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(5)

interp = ClassificationInterpretation.from_learner(learn)
print(interp.plot_confusion_matrix())

cleaner = ImageClassifierCleaner(learn)

for idx in cleaner.delete(): cleaner.fns[idx].unlink()
for idx,cat in cleaner.change(): shutil.move(str(cleaner.fns[idx]), path/cat)


learn.export()


path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')


#learn_inf.predict('/content/A032022.tif')