# shanesully
# Install and configure vim auto completion
#

echo "Setting up vim auto completion...n"

cd ~/.vim/bundle

echo "Downloading YouCompleteMe..."
{
    git clone https://github.com/Valloric/YouCompleteMe
} &> /dev/null

printf "Installing..."

cd YouCompleteMe

{
    git submodule update --init --recursive
    ./install.sh --clang-completer
} &> /dev/null

echo "Setup completed"

