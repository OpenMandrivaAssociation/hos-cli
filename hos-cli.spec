%global rootpath %{_datadir}/hos

Name:     hos-cli
Version:  0.1.20260128
Release:  1
Summary:  HouseOfSoftware CLI
License:  -
URL:      https://git.houseof.software/HouseOfSoftware/cli

BuildArch:  noarch

Source0:  %{name}-%{version}.tar.gz

Requires:  bash
Requires:  car
Requires:  curl

Recommends:  pv

%description
HouseOfSoftware's scripts for tasks such as uploading to the IPFS node.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{rootpath}
cp *.sh %{buildroot}/%{rootpath}/

%files
%{rootpath}/*
