# Script generated with Bloom
pkgdesc="ROS - The rbcar_sim package. It contains RBCAR simulation packages"
url='http://wiki.ros.org/rbcar_sim'

pkgname='ros-kinetic-rbcar-sim'
pkgver='1.0.4_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-rbcar-control'
'ros-kinetic-rbcar-gazebo'
'ros-kinetic-rbcar-joystick'
'ros-kinetic-rbcar-robot-control'
'ros-kinetic-rbcar-sim-bringup'
)

conflicts=()
replaces=()

_dir=rbcar_sim
source=()
md5sums=()

prepare() {
    cp -R $startdir/rbcar_sim $srcdir/rbcar_sim
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

