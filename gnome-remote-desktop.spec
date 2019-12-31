Name:           gnome-remote-desktop
Version:        0.1.6
Release:        4
Summary:        Screen share service of GNOME Remote Desktop

License:        GPLv2+
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        https://gitlab.gnome.org/jadahl/gnome-remote-desktop/uploads/c6862c12f0b741714d5a27e0693322fe/gnome-remote-desktop-0.1.6.tar.xz
Patch00001:     0001-vnc-Add-anonymous-TLS-encryption-support.patch
Patch00002:     0001-meson.build-Bump-pipewire-requirement-to-0.2.2.patch
Patch00003:     0001-session-vnc-Don-t-requeue-close-session-idle.patch
Patch00004:     0002-vnc-pipewire-stream-Close-session-when-disconnected.patch

BuildRequires:  meson >= 0.36.0 pkgconfig pkgconfig(glib-2.0) >= 2.32 pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(libpipewire-0.2) >= 0.2.2 pkgconfig(libvncserver) >= 0.9.11-7 pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libnotify) pkgconfig(gnutls) systemd

Requires:       pipewire >= 0.2.2

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
* Wed Dec 11 2019 daiqianwen <daiqianwen@huawei.com> - 0.1.6-3
- Package init

