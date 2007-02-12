%define		_splash		Lila

Summary:	KDE splash screen
Summary(pl.UTF-8):   Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=32797&id=1
Source0:	http://download.berlios.de/lila-theme/lila-kde-splash-20051222.tar.gz
# Source0-md5:	390143c73f258dbfaf42e25022cb106e
URL:		http://www.kde-look.org/content/show.php?content=32797
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice splash screen in shades of purple. For people who prefer mild
colors on their desktop.

%description -l pl.UTF-8
Ładny ekran startowy w odcieniach fioletu. Dla osób preferujących
łagodne kolory na swoim pulpicie.

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
