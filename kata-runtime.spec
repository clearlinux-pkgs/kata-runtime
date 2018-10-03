#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-runtime
Version  : 1.3.0
Release  : 21
URL      : https://github.com/kata-containers/runtime/archive/1.3.0.tar.gz
Source0  : https://github.com/kata-containers/runtime/archive/1.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception WTFPL
Requires: kata-runtime-bin = %{version}-%{release}
Requires: kata-runtime-config = %{version}-%{release}
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-add-fake-autogen.patch
Patch2: 0002-Add-Clear-Linux-Docker-integration-for-Kata-Containe.patch
Patch3: 0003-Set-kata-runtime-as-default-runtime-for-cri-o.patch

%description
[![Build Status](https://travis-ci.org/kata-containers/runtime.svg?branch=master)](https://travis-ci.org/kata-containers/runtime)
[![Build Status](http://jenkins.katacontainers.io/job/kata-containers-runtime-ubuntu-16-04-master/badge/icon)](http://jenkins.katacontainers.io/job/kata-containers-runtime-ubuntu-16-04-master/)
[![Go Report Card](https://goreportcard.com/badge/github.com/kata-containers/runtime)](https://goreportcard.com/report/github.com/kata-containers/runtime)
[![GoDoc](https://godoc.org/github.com/kata-containers/runtime?status.svg)](https://godoc.org/github.com/kata-containers/runtime)

%package bin
Summary: bin components for the kata-runtime package.
Group: Binaries
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-config = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}

%description bin
bin components for the kata-runtime package.


%package config
Summary: config components for the kata-runtime package.
Group: Default

%description config
config components for the kata-runtime package.


%package data
Summary: data components for the kata-runtime package.
Group: Data

%description data
data components for the kata-runtime package.


%package libexec
Summary: libexec components for the kata-runtime package.
Group: Default

%description libexec
libexec components for the kata-runtime package.


%package license
Summary: license components for the kata-runtime package.
Group: Default

%description license
license components for the kata-runtime package.


%prep
%setup -q -n runtime-1.3.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538420222
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/runtime" \
;cd "${GOPATH}/src/github.com/kata-containers/runtime"
make  %{?_smp_mflags} PREFIX=/usr/ DESTDIR=%{buildroot} QEMUPATH=/usr/bin/kata-qemu-lite-system-x86_64

%install
export SOURCE_DATE_EPOCH=1538420222
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-runtime
cp LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/clearcontainers/proxy/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_clearcontainers_proxy_COPYING
cp vendor/github.com/codahale/hdrhistogram/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_codahale_hdrhistogram_LICENSE
cp vendor/github.com/containerd/cri-containerd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cri-containerd_LICENSE
cp vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_cni_LICENSE
cp vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_plugins_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/dlespiau/covertool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_dlespiau_covertool_LICENSE
cp vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_docker_go-units_LICENSE
cp vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-ini_ini_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/grpc-ecosystem/grpc-opentracing/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_grpc-ecosystem_grpc-opentracing_LICENSE
cp vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_yamux_LICENSE
cp vendor/github.com/intel/govmm/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_intel_govmm_COPYING
cp vendor/github.com/kata-containers/agent/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_kata-containers_agent_LICENSE
cp vendor/github.com/kubernetes-incubator/cri-o/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_kubernetes-incubator_cri-o_LICENSE
cp vendor/github.com/mdlayher/vsock/LICENSE.md %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_mdlayher_vsock_LICENSE.md
cp vendor/github.com/mitchellh/mapstructure/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_mitchellh_mapstructure_LICENSE
cp vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runc_LICENSE
cp vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runtime-spec_LICENSE
cp vendor/github.com/opentracing/opentracing-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opentracing_opentracing-go_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/safchain/ethtool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_safchain_ethtool_LICENSE
cp vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_seccomp_libseccomp-golang_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/stretchr/testify/LICENCE.txt %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENCE.txt
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/uber/jaeger-client-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-client-go_LICENSE
cp vendor/github.com/uber/jaeger-lib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-lib_LICENSE
cp vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_urfave_cli_LICENSE
cp vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netlink_LICENSE
cp vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netns_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_text_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_grpc_LICENSE
cp virtcontainers/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/virtcontainers_LICENSE
cp virtcontainers/pkg/oci/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/virtcontainers_pkg_oci_LICENSE
%make_install PREFIX=/usr/ DESTDIR=%{buildroot} DESTCONFIG=%{buildroot}/usr/share/defaults/kata-containers/configuration.toml QEMUPATH=/usr/bin/kata-qemu-lite-system-x86_64
## install_append content
sed -i -e '/^initrd =/d' %{buildroot}/usr/share/defaults/kata-containers/configuration.toml
install -m 0755 -D set-docker-default-runtime %{buildroot}/usr/bin/set-docker-default-runtime
install -m 0644 -D clearlinux.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/clearlinux.conf
install -m 0644 -D 50-runtime.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/50-runtime.conf
install -m 0644 -D docker-set-runtime.service %{buildroot}/usr/lib/systemd/system/docker-set-runtime.service
install -m 0755 -D set-crio-default-runtime %{buildroot}/usr/bin/set-crio-default-runtime
install -m 0644 -D crio-clearlinux.conf %{buildroot}/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
install -m 0644 -D crio-set-runtime.service %{buildroot}/usr/lib/systemd/system/crio-set-runtime.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kata-collect-data.sh
/usr/bin/kata-runtime
/usr/bin/set-crio-default-runtime
/usr/bin/set-docker-default-runtime

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/crio-set-runtime.service
/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
/usr/lib/systemd/system/docker-set-runtime.service
/usr/lib/systemd/system/docker.service.d/50-runtime.conf
/usr/lib/systemd/system/docker.service.d/clearlinux.conf

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/kata-runtime
/usr/share/defaults/kata-containers/configuration.toml
/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENCE.txt

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-netmon

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/kata-runtime/LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_clearcontainers_proxy_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_codahale_hdrhistogram_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cri-containerd_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_cni_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_plugins_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_dlespiau_covertool_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_docker_go-units_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-ini_ini_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_grpc-ecosystem_grpc-opentracing_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_yamux_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_intel_govmm_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_kata-containers_agent_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_kubernetes-incubator_cri-o_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_mdlayher_vsock_LICENSE.md
/usr/share/package-licenses/kata-runtime/vendor_github.com_mitchellh_mapstructure_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runtime-spec_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opentracing_opentracing-go_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_safchain_ethtool_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_seccomp_libseccomp-golang_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-client-go_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-lib_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_urfave_cli_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netlink_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netns_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_grpc_LICENSE
/usr/share/package-licenses/kata-runtime/virtcontainers_LICENSE
/usr/share/package-licenses/kata-runtime/virtcontainers_pkg_oci_LICENSE
