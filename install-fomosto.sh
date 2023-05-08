# Download fomosto and install it
git clone https://git.pyrocko.org/pyrocko/fomosto-qseis.git
cd fomosto-qseis
autoreconf -i
./configure
make
sudo make install
