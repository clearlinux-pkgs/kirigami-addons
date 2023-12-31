#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: e661f3a
#
Name     : kirigami-addons
Version  : 0.9.0
Release  : 1
URL      : https://github.com/KDE/kirigami-addons/archive/refs/tags/v0.9.0.tar.gz
Source0  : https://github.com/KDE/kirigami-addons/archive/refs/tags/v0.9.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kirigami-addons-lib = %{version}-%{release}
Requires: kirigami-addons-license = %{version}-%{release}
Requires: kirigami-addons-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kirigami2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC-BY-SA-4.0
-->
# Kirigami Addons
A set of "widgets" i.e visual end user components along with a code to support them.
Components are usable by both touch and desktop experiences providing a native experience on both,
and look native with any QQC2 style (qqc2-desktop-theme, Material or Plasma)

%package dev
Summary: dev components for the kirigami-addons package.
Group: Development
Requires: kirigami-addons-lib = %{version}-%{release}
Provides: kirigami-addons-devel = %{version}-%{release}
Requires: kirigami-addons = %{version}-%{release}

%description dev
dev components for the kirigami-addons package.


%package lib
Summary: lib components for the kirigami-addons package.
Group: Libraries
Requires: kirigami-addons-license = %{version}-%{release}

%description lib
lib components for the kirigami-addons package.


%package license
Summary: license components for the kirigami-addons package.
Group: Default

%description license
license components for the kirigami-addons package.


%package locales
Summary: locales components for the kirigami-addons package.
Group: Default

%description locales
locales components for the kirigami-addons package.


%prep
%setup -q -n kirigami-addons-0.9.0
cd %{_builddir}/kirigami-addons-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701218785
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701218785
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami-addons
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
cp %{_builddir}/kirigami-addons-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kirigami-addons/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang kirigami-addons

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5KirigamiAddons/KF5KirigamiAddonsConfig.cmake
/usr/lib64/cmake/KF5KirigamiAddons/KF5KirigamiAddonsConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/ClockFace.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/DateInput.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/DatePicker.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/DatePopup.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/TimeInput.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/TimePicker.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/libdateandtimeplugin.so
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/private/ClockElement.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/private/DesktopDateInput.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/private/Hand.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/private/MobileDateInput.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/private/TumblerTimePicker.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/dateandtime/qmldir
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/AbstractMaximizeComponent.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/AlbumMaximizeComponent.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/AlbumModelItem.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/ImageMaximizeDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/SearchPopupField.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/VideoMaximizeDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/libcomponentsplugin.so
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/components/qmldir
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/AboutKDE.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/AboutPage.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/AbstractFormDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormArrow.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormButtonDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormCard.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormCardHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormCheckDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormComboBoxDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormDelegateBackground.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormDelegateSeparator.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormGridContainer.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormRadioDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormSectionText.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormSpinBoxDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormSwitchDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormTextDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/FormTextFieldDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/libmobileformplugin.so
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/private/ContentItemLoader.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/private/SpinButton.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/labs/mobileform/qmldir
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/sounds/SoundsPicker.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/sounds/libsoundsplugin.so
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/sounds/qmldir
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/AbstractTreeItem.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/BasicTreeItem.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/TreeListView.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/TreeTableView.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/TreeViewDecoration.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/libtreeviewplugin.so
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/private/InternalTreeListView.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/private/InternalTreeTableView.qml
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/qmldir
/usr/lib64/qt5/qml/org/kde/kirigamiaddons/treeview/styles/org.kde.desktop/TreeViewDecoration.qml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami-addons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kirigami-addons/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kirigami-addons/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kirigami-addons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kirigami-addons/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kirigami-addons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kirigami-addons/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/kirigami-addons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kirigami-addons/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/kirigami-addons/f26cccd93362d640ef2c05d1c52b5efe1620a9b2
/usr/share/package-licenses/kirigami-addons/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kirigami-addons.lang
%defattr(-,root,root,-)

