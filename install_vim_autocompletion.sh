# Setup YouCompleteMe

echo "Setting up vim auto completion..."

mkdir -p ~/.vim/bundle
cd ~/.vim/bundle

echo "Downloading YouCompleteMe..."
{
    git clone https://github.com/Valloric/YouCompleteMe
} &> /dev/null

echo "Installing..."

cd YouCompleteMe

{
    git submodule update --init --recursive
    ./install.sh --clang-completer
} &> /dev/null

echo "Setup completed"

