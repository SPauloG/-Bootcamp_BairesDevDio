// Função para ler uma imagem
function [img] = read_image(file_path)
    img = imread(file_path);
endfunction

// Função para salvar uma imagem
function write_image(file_path, img)
    imwrite(img, file_path);
endfunction

// Função para criar uma pasta de saída
function [folder_path] = create_output_folder(folder_name)
    folder_path = folder_name;
    if ~isdir(folder_path) then
        mkdir(folder_path);
    end
endfunction

// Função para converter para escala de cinza
function [gray_img] = convert_to_grayscale(img)
    if size(img, 3) == 3 then
        gray_img = rgb2gray(img);
    else
        gray_img = img;
    end
endfunction

// Função para binarizar a imagem
function [binary_img] = binarize(img, threshold)
    binary_img = img > threshold;
endfunction

// Função principal
function main()
    // Solicita ao usuário o caminho da imagem de entrada
    input_file = input("Digite o caminho da imagem de entrada: ", "string");
    
    // Verifica se o arquivo existe
    if ~isfile(input_file) then
        disp("Erro: O arquivo não foi encontrado.");
        return;
    end
    
    // Lê a imagem
    img = read_image(input_file);
    
    // Obtém as dimensões da imagem
    [height, width, channels] = size(img);
    disp("Largura: " + string(width) + " pixels");
    disp("Altura: " + string(height) + " pixels");
    
    // Converte para escala de cinza
    gray_img = convert_to_grayscale(img);
    
    // Converte para binário
    binary_img = binarize(gray_img, 128);
    
    // Cria a pasta de saída
    output_folder = create_output_folder("output");
    
    // Salva as imagens processadas
    write_image(fullfile(output_folder, "grayscale.jpg"), gray_img);
    write_image(fullfile(output_folder, "binary.jpg"), binary_img);
    
    disp("Imagens processadas salvas em: " + output_folder);
endfunction

// Executa a função principal
main();
