# TODO:
# - some icon
%define		_origname	race
Summary:	OpenGL Racing Game
Summary(pl):	Gra wy¶cigowa w OpenGL
Name:		raceGL
Version:	0.5
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	ftp://users.freebsd.org.uk/pub/foobar2k/%{_origname}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://projectz.ath.cx/?id=70
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_gamedata	%{_datadir}/%{name}/data/

%description
OpenGL Racing Game is a Star Wars: Racer style game coded in pure C
using OpenGL. You can race round and round to your heart's desire.
Features include Heightfield map loading, texture mapping, a
speedometer, a translucent radar map, a timer, music, sound.

%description -l pl
OpenGL Racing Game jest gr± w stylu Star Wars: Racer napisan± w
czystym C przy u¿yciu OpenGL. Mo¿esz je¼dziæ sobie w kó³ko ile ci siê
podoba. Cechy: Heightfield map loading, mapowanie tekstur,
prêdko¶ciomierz, przezroczysta mapa radarowa, czasomierz, muzyka,
d¼wiêk.

%prep
%setup -q -n %{_origname}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_gamedata}/{all,desert,models,music,sea,sounds}}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games/Racing

install %{_origname}	$RPM_BUILD_ROOT%{_datadir}/%{name}/
install config		$RPM_BUILD_ROOT%{_datadir}/%{name}/
install data/all/*	$RPM_BUILD_ROOT%{_gamedata}/all/
install data/desert/*	$RPM_BUILD_ROOT%{_gamedata}/desert/
install data/models/*	$RPM_BUILD_ROOT%{_gamedata}/models/
install data/music/*	$RPM_BUILD_ROOT%{_gamedata}/music/
install data/sea/*	$RPM_BUILD_ROOT%{_gamedata}/sea/
install data/sounds/*	$RPM_BUILD_ROOT%{_gamedata}/sounds/

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
# Initialization script:

cd %{_datadir}/%{name}/
./%{_origname}
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Racing

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/%{_origname}
%attr(644,root,root) %config(noreplace) %{_datadir}/%{name}/config
%attr(644,root,root) %{_gamedata}/all/*
%attr(644,root,root) %{_gamedata}/desert/*
%attr(644,root,root) %{_gamedata}/models/*
%attr(644,root,root) %{_gamedata}/music/*
%attr(644,root,root) %{_gamedata}/sea/*
%attr(644,root,root) %{_gamedata}/sounds/*
%dir %{_datadir}/%{name}
%dir %{_gamedata}
%dir %{_gamedata}/all
%dir %{_gamedata}/desert
%dir %{_gamedata}/models
%dir %{_gamedata}/music
%dir %{_gamedata}/sea
%dir %{_gamedata}/sounds
%{_applnkdir}/Games/Racing/*.desktop
#%{_pixmapsdir}/*
