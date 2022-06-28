%global systemd_unit gnome-remote-desktop.service

Name:           gnome-remote-desktop
Version:        42.2
Release:        1
Summary:        Screen share service of GNOME Remote Desktop
License:        GPLv2+
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/gnome-remote-desktop/40/%{name}-%{version}.tar.xz

Patch0:         gnutls-anontls.patch
Patch1:         0001-Add-man-page.patch

BuildRequires:  meson pkgconfig gcc asciidoc systemd freerdp-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.32 pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0 pkgconfig(libvncserver) pkgconfig(libvncclient) pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libnotify) pkgconfig(gnutls) pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gudev-1.0)

Requires:       pipewire >= 0.3.0
Requires:       libdrm
Requires:       libepoxy

Obsoletes:      vino < 3.22.0-21

%description
GNOME Remote Desktop is a remote desktop daemon for GNOME using pipewire.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang gnome-remote-desktop

%post
%systemd_user_post %{systemd_unit}

%preun
%systemd_user_preun %{systemd_unit}

%postun
%systemd_user_postun_with_restart %{systemd_unit}

%files -f gnome-remote-desktop.lang
%license COPYING
%doc README
%{_bindir}/grdctl
%{_libexecdir}/gnome-remote-desktop-daemon
%{_userunitdir}/gnome-remote-desktop.service
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%{_datadir}/gnome-remote-desktop/
%{_mandir}/man1/grdctl.1*

%changelog
* Fri Jun 24 2022 weijin deng <weijin.deng@turbolinux.com.cn> - 42.2-1
- Update to 42.2

* Mon Mar 28 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 42.0-1
- Update to 42.0

* Mon Apr 18 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 0.1.9-3
- Add gnome-remote-desktop.yaml

* Mon Sep 27 2021 Wenlong Ding <wenlong.ding@turbolinux.com.cn> - 0.1.9-2
- Add 2 patch to fix core-dump when start gnome-remote-desktop.service

* Wed Jun 30 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 0.1.9-1
- Upgrade to 0.1.9
- Delete patches whose content existed or target patch file not existed in this version 0.1.9
- Modify 0001-vnc-Add-anonymous-TLS-encryption-support.patch

* Wed Dec 11 2019 daiqianwen <daiqianwen@huawei.com> - 0.1.6-3
- Package init
