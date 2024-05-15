#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x02325448204E452A (carl@carlschwan.eu)
#
Name     : kirigami-addons
Version  : 1.2.1
Release  : 7
URL      : https://download.kde.org/stable/kirigami-addons/kirigami-addons-1.2.1.tar.xz
Source0  : https://download.kde.org/stable/kirigami-addons/kirigami-addons-1.2.1.tar.xz
Source1  : https://download.kde.org/stable/kirigami-addons/kirigami-addons-1.2.1.tar.xz.sig
Source2  : 02325448204E452A.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kirigami-addons-lib = %{version}-%{release}
Requires: kirigami-addons-license = %{version}-%{release}
Requires: kirigami-addons-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC-BY-SA-4.0
-->
Kirigami Addons is an additional set of visual components that work well on mobile and desktop and are guaranteed to be cross-platform. It uses Kirigami under the hood to create its components and should look native with any QtQuick Controls style.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 02325448204E452A' gpg.status
%setup -q -n kirigami-addons-1.2.1
cd %{_builddir}/kirigami-addons-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715783186
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
export GOAMD64=v2
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
export SOURCE_DATE_EPOCH=1715783186
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami-addons
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/cbca59e0e62dd8bfc0468847678552cadebea0a9 || :
cp %{_builddir}/kirigami-addons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kirigami-addons/cbca59e0e62dd8bfc0468847678552cadebea0a9 || :
cp %{_builddir}/kirigami-addons-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kirigami-addons/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kirigami-addons6

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF6KirigamiAddons/KF6KirigamiAddonsConfig.cmake
/usr/lib64/cmake/KF6KirigamiAddons/KF6KirigamiAddonsConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/Avatar.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/AvatarButton.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/Banner.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/BottomDrawer.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/DialogRoundedBackground.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/DoubleFloatingButton.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/FloatingButton.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/FloatingToolBar.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/MessageDialog.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/SearchPopupField.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/SegmentedButton.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/componentsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/libcomponentsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/components/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/DatePopup.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/TimePicker.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/TimePopup.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/dateandtimeplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/libdateandtimeplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePathView.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePicker.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePickerDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/dateandtime/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/DefaultContentItem.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/IndicatorItemDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/RoundedItemDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/RoundedTreeDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/SubtitleContentItem.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/delegatesplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/libdelegatesplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/delegates/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/AboutKDE.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/AboutPage.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/AbstractFormDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormArrow.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormButtonDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormCard.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormCardDialog.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormCardPage.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormCheckDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormColorDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormComboBoxDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormDateTimeDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormDelegateBackground.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormDelegateSeparator.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormGridContainer.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormPasswordFieldDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormRadioDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormSectionText.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormSpinBoxDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormSwitchDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormTextDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/FormTextFieldDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/formcardplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/libformcardplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/private/ContentItemLoader.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/private/SpinButton.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/formcard/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/AbstractMaximizeComponent.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/AlbumMaximizeComponent.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/AlbumModelItem.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/Avatar.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/Banner.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/DialogRoundedBackground.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/DownloadAction.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/ImageMaximizeDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/SearchPopupField.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/VideoMaximizeDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/componentslabsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/libcomponentslabsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/labs/components/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/CategorizedSettings.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/SettingAction.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/libsettingsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/settings/settingsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/sounds/SoundsPicker.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/sounds/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/sounds/libsoundsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/sounds/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/sounds/soundsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/HeaderComponent.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/KTableView.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/ListTableView.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/libtableviewplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/AbstractHeaderComponent.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/AbstractTable.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/HeaderDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/ListCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/ListRowDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/private/TableCellDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/tableview/tableviewplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/TreeViewDecoration.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/libtreeviewplugin.so
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/qmldir
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/styles/org.kde.desktop/TreeViewDecoration.qml
/usr/lib64/qt6/qml/org/kde/kirigamiaddons/treeview/treeviewplugin.qmltypes

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami-addons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kirigami-addons/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/kirigami-addons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kirigami-addons/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kirigami-addons/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kirigami-addons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kirigami-addons/cbca59e0e62dd8bfc0468847678552cadebea0a9
/usr/share/package-licenses/kirigami-addons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kirigami-addons/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/kirigami-addons/f26cccd93362d640ef2c05d1c52b5efe1620a9b2
/usr/share/package-licenses/kirigami-addons/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kirigami-addons6.lang
%defattr(-,root,root,-)

