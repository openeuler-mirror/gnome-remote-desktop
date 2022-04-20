Name:           gnome-remote-desktop
Version:        0.1.9
Release:        3
Summary:        Screen share service of GNOME Remote Desktop

License:        GPLv2+
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/gnome-remote-desktop/0.1/%{name}-%{version}.tar.xz
Patch00001:     0001-vnc-Drop-frames-if-client-is-gone.patch
Patch00002:     0001-vnc-Add-anonymous-TLS-encryption-support.patch
Patch00003:     0001-vnc-Copy-pixels-using-the-right-destination-stride.patch
BuildRequires:  meson >= 0.47.0 pkgconfig pkgconfig(glib-2.0) >= 2.32 pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0 pkgconfig(libvncserver) >= 0.9.11-7 pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libnotify) pkgconfig(gnutls) systemd pkgconfig(freerdp2)

Requires:       pipewire >= 0.3.0

%description
GNOME Remote Desktop is a remote desktop daemon for GNOME using pipewire.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post gnome-remote-desktop.service

%preun
%systemd_user_preun gnome-remote-desktop.service

%postun
%systemd_user_postun_with_restart gnome-remote-desktop.service

%files
%doc README COPYING
%{_libexecdir}/gnome-remote-desktop-daemon
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.{gschema.xml,enums.xml}
%{_userunitdir}/gnome-remote-desktop.service

%changelog
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
