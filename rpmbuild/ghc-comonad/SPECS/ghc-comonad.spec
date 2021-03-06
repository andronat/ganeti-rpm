# cabal2spec-0.25
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name comonad

%global common_summary Haskell %{pkg_name} library

%global common_description A %{pkg_name} library for Haskell.

Name:           ghc-%{pkg_name}
Version:        4.2.2
Release:        2%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        BSD
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
#ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec

BuildRequires: ghc-compiler
BuildRequires: ghc-contravariant-devel
BuildRequires: ghc-distributive-devel
BuildRequires: ghc-semigroups-devel
BuildRequires: ghc-tagged-devel
BuildRequires: ghc-transformers-devel
BuildRequires: ghc-transformers-compat-devel

Requires: ghc

%description
%{common_description}


%package devel
Summary:        %{common_summary} development files
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files


%changelog
* Fri Jan  9 2015 Jun Futagawa <jfut@integ.jp> - 4.2.2-2
- Rebuild for ghc-transformers-compat update

* Tue Aug  5 2014 Jun Futagawa <jfut@integ.jp> - 4.2.2-1
- Removed ExclusiveArch
- Removed ghc_devel_package

* Tue Aug  5 2014 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.5
