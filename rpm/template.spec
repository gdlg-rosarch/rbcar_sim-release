Name:           ros-kinetic-rbcar-sim
Version:        1.0.4
Release:        1%{?dist}
Summary:        ROS rbcar_sim package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rbcar_sim
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rbcar-control
Requires:       ros-kinetic-rbcar-gazebo
Requires:       ros-kinetic-rbcar-joystick
Requires:       ros-kinetic-rbcar-robot-control
Requires:       ros-kinetic-rbcar-sim-bringup
BuildRequires:  ros-kinetic-catkin

%description
The rbcar_sim package. It contains RBCAR simulation packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 05 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.4-1
- Autogenerated by Bloom

* Fri Jul 15 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.4-0
- Autogenerated by Bloom

