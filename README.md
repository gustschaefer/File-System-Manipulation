# File System Manipulation

Programa que recebe quatro parâmetros: 

1. Um diretório de imagens.
2. Um diretório destino onde as imagens serão armazenadas.
3. O tamanho que as imagens serão redimensionadas.
4. Tamanho mínimo da imagem. 

O sistema le as imagens do diretório de origem, redimensiona cada uma de acordo com as orientações, e grava no diretório destino. Manipulações:

* Serão redimensionadas apenas as imagens com tamanho (largura ou altura) maior que o tamanho mínimo da imagem recebido por parâmetro. Imagens que não atendem esse a critério devem ser ignoradas.
* O redimensionamento da imagem deverá ser proporcional ao maior tamanho (largura ou altura) da imagem. Por exemplo: dado uma imagem de tamanho 180x120 e o tamanho mínimo recebido é 150, a imagem final será 150x100.
* Um arquivo imagens.txt deverá ser criado para armazenar o nome e a classe das imagens redimensionadas. Cada linha do arquivo deverá ter a seguinte estrutura: nome_imagem,classe
* Um arquivo imagens_desconsideradas.txt deverá ser criado para armazenar o nome e o tamanho original das imagens não processadas. Cada linha do arquivo deverá ter a seguinte estrutura: nome_imagem, largura, altura.
