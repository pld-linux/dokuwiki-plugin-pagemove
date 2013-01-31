%define		plugin		pagemove
Summary:	DokuWiki PageMove plugin
Summary(pl.UTF-8):	Wtyczka PageMove dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20130125
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/michitux/DokuWiki-Pagemove-Plugin/archive/master.tar.gz?/%{plugin}-%{version}.tgz
# Source0-md5:	7224d4641568b766299be6a29688d134
URL:		http://www.dokuwiki.org/plugin:pagemove
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	dokuwiki >= 20120919
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin is designed for moving and renaming pages within your Wiki
whilst maintaining the integrity of links to and from the page.

In full you can:
- Rename a page.
- Move a page to an existing namspace.
- Move a page to a new namespace.
- A combination of the above.

%description -l pl.UTF-8
Ta wtyczka służy do przesuwania i zmiany nazw stron wewnątrz Wiki z
zachowaniem integralności odnośników z i do strony.

W zupełności można:
- usunąć stronę,
- przenieść stronę do istniejącej przestrzeni nazw,
- przenieść stronę do nowej przestrzeni nazw,
- wykonać połączenie powyższych.

%prep
%setup -qc
mv DokuWiki-Pagemove-Plugin-*/* .
%{__rm} DokuWiki-Pagemove-Plugin-*/.git*

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%{__rm} $RPM_BUILD_ROOT%{plugindir}/README
%{__rm} -r $RPM_BUILD_ROOT%{plugindir}/_test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/*.js
%dir %{plugindir}/lang
%{plugindir}/lang/en
%lang(cs) %{plugindir}/lang/cs
%lang(de) %{plugindir}/lang/de
%lang(es) %{plugindir}/lang/es
%lang(fr) %{plugindir}/lang/fr
%lang(lv) %{plugindir}/lang/lv
%lang(nl) %{plugindir}/lang/nl
%lang(pl) %{plugindir}/lang/pl
%lang(ru) %{plugindir}/lang/ru
%lang(sl) %{plugindir}/lang/sl
%lang(zh_CN) %{plugindir}/lang/zh
