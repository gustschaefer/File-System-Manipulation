import func as f

input_dir = "/your/input/dir/path"
new_dir = "your/out/dir/path"
new_size = (710, 405)
min_size = 710

classes = ['Human', 'Skull', 'Zombie']
all_not_resized = []
all_resized = []

if f.check_dir(new_dir) == False:
	os.mkdir(new_dir) # cria uma nova pasta se a pasta destino nao existe

all_resized, all_not_resized = f.resize(input_dir, new_dir, new_size, min_size, classes)


f.create_txt("../imagens.txt", all_resized)
f.create_txt("../desconsideradas.txt", all_not_resized)