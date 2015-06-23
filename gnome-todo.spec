Name:          gnome-todo
Version:       3.17.3
Release:       1%{?dist}
Summary:       Personal task manager for GNOME

License:       GPLv3+
URL:           https://git.gnome.org/browse/gnome-todo/
Source0:       https://download.gnome.org/sources/%{name}/3.17/%{name}-%{version}.tar.xz 
# https://git.gnome.org/browse/gnome-todo/commit/?id=8a37f68f046962d98c44a586ec3eed6dab43564d
Patch0:        0001-desktop-drop-Extra-category-it-s-doesn-t-exist.patch

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libecal-1.2)
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: pkgconfig(libical)
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util
#Requires:	

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%prep
%autosetup -S git

%build
%configure
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Todo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/org.gnome.Todo.appdata.xml

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%license COPYING
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/appdata/org.gnome.Todo.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml	

%changelog
* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.17.3-1
- Initial package
