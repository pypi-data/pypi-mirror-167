#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/ndarray.hpp>
#include <pythonic/include/types/complex128.hpp>
#include <pythonic/include/types/float64.hpp>
#include <pythonic/types/complex128.hpp>
#include <pythonic/types/ndarray.hpp>
#include <pythonic/types/float64.hpp>
#include <pythonic/include/builtins/None.hpp>
#include <pythonic/include/builtins/abs.hpp>
#include <pythonic/include/builtins/getattr.hpp>
#include <pythonic/include/builtins/int_.hpp>
#include <pythonic/include/builtins/len.hpp>
#include <pythonic/include/builtins/pythran/make_shape.hpp>
#include <pythonic/include/builtins/range.hpp>
#include <pythonic/include/builtins/round.hpp>
#include <pythonic/include/builtins/tuple.hpp>
#include <pythonic/include/numpy/sqrt.hpp>
#include <pythonic/include/numpy/zeros.hpp>
#include <pythonic/include/operator_/add.hpp>
#include <pythonic/include/operator_/div.hpp>
#include <pythonic/include/operator_/ge.hpp>
#include <pythonic/include/operator_/iadd.hpp>
#include <pythonic/include/operator_/isub.hpp>
#include <pythonic/include/operator_/mul.hpp>
#include <pythonic/include/operator_/sub.hpp>
#include <pythonic/include/types/complex.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/builtins/None.hpp>
#include <pythonic/builtins/abs.hpp>
#include <pythonic/builtins/getattr.hpp>
#include <pythonic/builtins/int_.hpp>
#include <pythonic/builtins/len.hpp>
#include <pythonic/builtins/pythran/make_shape.hpp>
#include <pythonic/builtins/range.hpp>
#include <pythonic/builtins/round.hpp>
#include <pythonic/builtins/tuple.hpp>
#include <pythonic/numpy/sqrt.hpp>
#include <pythonic/numpy/zeros.hpp>
#include <pythonic/operator_/add.hpp>
#include <pythonic/operator_/div.hpp>
#include <pythonic/operator_/ge.hpp>
#include <pythonic/operator_/iadd.hpp>
#include <pythonic/operator_/isub.hpp>
#include <pythonic/operator_/mul.hpp>
#include <pythonic/operator_/sub.hpp>
#include <pythonic/types/complex.hpp>
#include <pythonic/types/str.hpp>
namespace __pythran_operators
{
  struct __transonic__
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type0>())) __type1;
      typedef typename pythonic::returnable<__type1>::type __type2;
      typedef __type2 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
    struct type
    {
      typedef std::complex<double> __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type1;
      typedef __type1 __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type3;
      typedef __type3 __type4;
      typedef decltype(pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type4>())) __type5;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type6;
      typedef __type6 __type7;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type8;
      typedef __type8 __type9;
      typedef decltype(pythonic::operator_::mul(std::declval<__type7>(), std::declval<__type9>())) __type10;
      typedef decltype(pythonic::operator_::sub(std::declval<__type5>(), std::declval<__type10>())) __type11;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type11>())) __type12;
      typedef typename pythonic::returnable<__type12>::type __type13;
      typedef __type13 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& vx_fft, argument_type3&& vy_fft) const
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin
  {
    typedef void callable;
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 , typename argument_type7 , typename argument_type8 >
    struct type
    {
      typedef std::complex<double> __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
      typedef __type1 __type2;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type3;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type4;
      typedef __type4 __type5;
      typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type5>())) __type6;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type6>::type>::type __type7;
      typedef typename pythonic::lazy<__type7>::type __type8;
      typedef __type8 __type9;
      typedef decltype(std::declval<__type3>()(std::declval<__type9>())) __type10;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type10>::type::iterator>::value_type>::type __type11;
      typedef __type11 __type12;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type6>::type>::type __type13;
      typedef typename pythonic::lazy<__type13>::type __type14;
      typedef __type14 __type15;
      typedef decltype(std::declval<__type3>()(std::declval<__type15>())) __type16;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type16>::type::iterator>::value_type>::type __type17;
      typedef __type17 __type18;
      typedef typename std::tuple_element<2,typename std::remove_reference<__type6>::type>::type __type19;
      typedef typename pythonic::lazy<__type19>::type __type20;
      typedef __type20 __type21;
      typedef decltype(std::declval<__type3>()(std::declval<__type21>())) __type22;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type22>::type::iterator>::value_type>::type __type23;
      typedef __type23 __type24;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type12>(), std::declval<__type18>(), std::declval<__type24>())) __type25;
      typedef decltype(std::declval<__type2>()[std::declval<__type25>()]) __type26;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type27;
      typedef __type27 __type28;
      typedef decltype(std::declval<__type28>()[std::declval<__type25>()]) __type33;
      typedef decltype(pythonic::operator_::mul(std::declval<__type26>(), std::declval<__type33>())) __type34;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type35;
      typedef __type35 __type36;
      typedef decltype(std::declval<__type36>()[std::declval<__type25>()]) __type41;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type42;
      typedef __type42 __type43;
      typedef decltype(std::declval<__type43>()[std::declval<__type25>()]) __type48;
      typedef decltype(pythonic::operator_::mul(std::declval<__type41>(), std::declval<__type48>())) __type49;
      typedef decltype(pythonic::operator_::sub(std::declval<__type34>(), std::declval<__type49>())) __type50;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type50>())) __type51;
      typedef __type51 __type52;
      typedef __type25 __type57;
      typedef pythonic::types::none_type __type58;
      typedef typename pythonic::returnable<__type58>::type __type59;
      typedef __type52 __ptype0;
      typedef __type57 __ptype1;
      typedef __type59 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 , typename argument_type7 , typename argument_type8 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6, argument_type7, argument_type8>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft, argument_type6&& rotxfft, argument_type7&& rotyfft, argument_type8&& rotzfft) const
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    struct type
    {
      typedef std::complex<double> __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
      typedef __type1 __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type3;
      typedef __type3 __type4;
      typedef decltype(pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type4>())) __type5;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type6;
      typedef __type6 __type7;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type8;
      typedef __type8 __type9;
      typedef decltype(pythonic::operator_::mul(std::declval<__type7>(), std::declval<__type9>())) __type10;
      typedef decltype(pythonic::operator_::sub(std::declval<__type5>(), std::declval<__type10>())) __type11;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type11>())) __type12;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type14;
      typedef __type14 __type15;
      typedef decltype(pythonic::operator_::mul(std::declval<__type7>(), std::declval<__type15>())) __type16;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type17;
      typedef __type17 __type18;
      typedef decltype(pythonic::operator_::mul(std::declval<__type18>(), std::declval<__type4>())) __type20;
      typedef decltype(pythonic::operator_::sub(std::declval<__type16>(), std::declval<__type20>())) __type21;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type21>())) __type22;
      typedef decltype(pythonic::operator_::mul(std::declval<__type18>(), std::declval<__type9>())) __type25;
      typedef decltype(pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type15>())) __type28;
      typedef decltype(pythonic::operator_::sub(std::declval<__type25>(), std::declval<__type28>())) __type29;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type29>())) __type30;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type12>(), std::declval<__type22>(), std::declval<__type30>())) __type31;
      typedef typename pythonic::returnable<__type31>::type __type32;
      typedef __type32 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft) const
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    struct type
    {
      typedef std::complex<double> __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type1;
      typedef __type1 __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type3;
      typedef __type3 __type4;
      typedef decltype(pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type4>())) __type5;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type6;
      typedef __type6 __type7;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type8;
      typedef __type8 __type9;
      typedef decltype(pythonic::operator_::mul(std::declval<__type7>(), std::declval<__type9>())) __type10;
      typedef decltype(pythonic::operator_::add(std::declval<__type5>(), std::declval<__type10>())) __type11;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type12;
      typedef __type12 __type13;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type14;
      typedef __type14 __type15;
      typedef decltype(pythonic::operator_::mul(std::declval<__type13>(), std::declval<__type15>())) __type16;
      typedef decltype(pythonic::operator_::add(std::declval<__type11>(), std::declval<__type16>())) __type17;
      typedef decltype(pythonic::operator_::mul(std::declval<__type0>(), std::declval<__type17>())) __type18;
      typedef typename pythonic::returnable<__type18>::type __type19;
      typedef __type19 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft) const
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__project_perpk3d
  {
    typedef void callable;
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type1;
      typedef __type1 __type2;
      typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type2>())) __type3;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type3>::type>::type __type4;
      typedef typename pythonic::lazy<__type4>::type __type5;
      typedef __type5 __type6;
      typedef decltype(std::declval<__type0>()(std::declval<__type6>())) __type7;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type7>::type::iterator>::value_type>::type __type8;
      typedef __type8 __type9;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type3>::type>::type __type10;
      typedef typename pythonic::lazy<__type10>::type __type11;
      typedef __type11 __type12;
      typedef decltype(std::declval<__type0>()(std::declval<__type12>())) __type13;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type13>::type::iterator>::value_type>::type __type14;
      typedef __type14 __type15;
      typedef typename std::tuple_element<2,typename std::remove_reference<__type3>::type>::type __type16;
      typedef typename pythonic::lazy<__type16>::type __type17;
      typedef __type17 __type18;
      typedef decltype(std::declval<__type0>()(std::declval<__type18>())) __type19;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type19>::type::iterator>::value_type>::type __type20;
      typedef __type20 __type21;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type9>(), std::declval<__type15>(), std::declval<__type21>())) __type22;
      typedef indexable<__type22> __type23;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type24;
      typedef __type24 __type25;
      typedef decltype(std::declval<__type25>()[std::declval<__type22>()]) __type30;
      typedef decltype(std::declval<__type2>()[std::declval<__type22>()]) __type42;
      typedef decltype(pythonic::operator_::mul(std::declval<__type30>(), std::declval<__type42>())) __type43;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type44;
      typedef __type44 __type45;
      typedef decltype(std::declval<__type45>()[std::declval<__type22>()]) __type50;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type51;
      typedef __type51 __type63;
      typedef decltype(std::declval<__type63>()[std::declval<__type22>()]) __type68;
      typedef decltype(pythonic::operator_::mul(std::declval<__type50>(), std::declval<__type68>())) __type69;
      typedef decltype(pythonic::operator_::add(std::declval<__type43>(), std::declval<__type69>())) __type70;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type71;
      typedef __type71 __type72;
      typedef decltype(std::declval<__type72>()[std::declval<__type22>()]) __type77;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type6>::type>::type __type78;
      typedef __type78 __type90;
      typedef decltype(std::declval<__type90>()[std::declval<__type22>()]) __type95;
      typedef decltype(pythonic::operator_::mul(std::declval<__type77>(), std::declval<__type95>())) __type96;
      typedef decltype(pythonic::operator_::add(std::declval<__type70>(), std::declval<__type96>())) __type97;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type98;
      typedef __type98 __type99;
      typedef decltype(std::declval<__type99>()[std::declval<__type22>()]) __type104;
      typedef decltype(pythonic::operator_::mul(std::declval<__type97>(), std::declval<__type104>())) __type105;
      typedef typename pythonic::assignable<__type105>::type __type106;
      typedef __type106 __type107;
      typedef decltype(pythonic::operator_::mul(std::declval<__type77>(), std::declval<__type107>())) __type108;
      typedef container<typename std::remove_reference<__type108>::type> __type109;
      typedef typename __combined<__type78,__type23,__type109>::type __type110;
      typedef decltype(pythonic::operator_::mul(std::declval<__type50>(), std::declval<__type107>())) __type112;
      typedef container<typename std::remove_reference<__type112>::type> __type113;
      typedef typename __combined<__type51,__type23,__type113>::type __type114;
      typedef decltype(pythonic::operator_::mul(std::declval<__type30>(), std::declval<__type107>())) __type116;
      typedef container<typename std::remove_reference<__type116>::type> __type117;
      typedef typename __combined<__type1,__type23,__type117>::type __type118;
      typedef __type22 __type119;
      typedef pythonic::types::none_type __type121;
      typedef typename pythonic::returnable<__type121>::type __type122;
      typedef __type119 __ptype12;
      typedef __type119 __ptype13;
      typedef __type122 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& self_inv_K_square_nozero, argument_type4&& vx_fft, argument_type5&& vy_fft, argument_type6&& vz_fft) const
    ;
  }  ;
  struct __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop
  {
    typedef void callable;
    typedef void pure;
    struct type
    {
      typedef pythonic::types::str __type0;
      typedef typename pythonic::returnable<__type0>::type __type1;
      typedef __type1 result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  struct __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop
  {
    typedef void callable;
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type6>::type>::type __type0;
      typedef __type0 __type1;
      typedef __type1 __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type3;
      typedef __type3 __type4;
      typedef __type4 __type5;
      typedef pythonic::types::none_type __type6;
      typedef typename pythonic::returnable<__type6>::type __type7;
      typedef __type2 __ptype24;
      typedef __type5 __ptype25;
      typedef __type7 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6>::result_type operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& self_inv_K_square_nozero, argument_type4&& vx_fft, argument_type5&& vy_fft, argument_type6&& vz_fft) const
    ;
  }  ;
  struct loop_spectra_kzkh
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type0;
      typedef __type0 __type1;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type1>::type>::type __type2;
      typedef __type2 __type3;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type4;
      typedef __type4 __type5;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type5>::type>::type __type6;
      typedef __type6 __type7;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type8;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::pythran::functor::make_shape{})>::type>::type __type9;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::len{})>::type>::type __type10;
      typedef std::integral_constant<long,1> __type11;
      typedef indexable_container<__type11, typename std::remove_reference<__type6>::type> __type12;
      typedef typename __combined<__type4,__type12>::type __type13;
      typedef __type13 __type14;
      typedef decltype(std::declval<__type10>()(std::declval<__type14>())) __type15;
      typedef typename pythonic::assignable<__type15>::type __type16;
      typedef __type16 __type17;
      typedef indexable_container<__type11, typename std::remove_reference<__type2>::type> __type18;
      typedef typename __combined<__type0,__type18>::type __type19;
      typedef __type19 __type20;
      typedef decltype(std::declval<__type10>()(std::declval<__type20>())) __type21;
      typedef typename pythonic::assignable<__type21>::type __type22;
      typedef __type22 __type23;
      typedef decltype(std::declval<__type9>()(std::declval<__type17>(), std::declval<__type23>())) __type24;
      typedef decltype(std::declval<__type8>()(std::declval<__type24>())) __type25;
      typedef typename pythonic::assignable<__type25>::type __type26;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::int_{})>::type>::type __type27;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::round{})>::type>::type __type28;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::abs{})>::type>::type __type29;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type30;
      typedef __type30 __type31;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type32;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type33;
      typedef __type33 __type34;
      typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type34>())) __type35;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type35>::type>::type __type36;
      typedef typename pythonic::lazy<__type36>::type __type37;
      typedef __type37 __type38;
      typedef decltype(std::declval<__type32>()(std::declval<__type38>())) __type39;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type39>::type::iterator>::value_type>::type __type40;
      typedef __type40 __type41;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type35>::type>::type __type42;
      typedef typename pythonic::lazy<__type42>::type __type43;
      typedef __type43 __type44;
      typedef decltype(std::declval<__type32>()(std::declval<__type44>())) __type45;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type45>::type::iterator>::value_type>::type __type46;
      typedef __type46 __type47;
      typedef typename std::tuple_element<2,typename std::remove_reference<__type35>::type>::type __type48;
      typedef typename pythonic::lazy<__type48>::type __type49;
      typedef __type49 __type50;
      typedef decltype(std::declval<__type32>()(std::declval<__type50>())) __type51;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type51>::type::iterator>::value_type>::type __type52;
      typedef __type52 __type53;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type41>(), std::declval<__type47>(), std::declval<__type53>())) __type54;
      typedef decltype(std::declval<__type31>()[std::declval<__type54>()]) __type55;
      typedef decltype(std::declval<__type29>()(std::declval<__type55>())) __type56;
      typedef typename pythonic::assignable<__type6>::type __type57;
      typedef __type57 __type58;
      typedef decltype(pythonic::operator_::div(std::declval<__type56>(), std::declval<__type58>())) __type59;
      typedef decltype(std::declval<__type28>()(std::declval<__type59>())) __type60;
      typedef decltype(std::declval<__type27>()(std::declval<__type60>())) __type61;
      typedef typename pythonic::lazy<__type61>::type __type62;
      typedef long __type64;
      typedef decltype(pythonic::operator_::sub(std::declval<__type17>(), std::declval<__type64>())) __type65;
      typedef typename pythonic::lazy<__type65>::type __type66;
      typedef typename __combined<__type62,__type66>::type __type67;
      typedef __type67 __type68;
      typedef decltype(pythonic::operator_::sub(std::declval<__type23>(), std::declval<__type64>())) __type70;
      typedef typename pythonic::lazy<__type70>::type __type71;
      typedef __type71 __type72;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type68>(), std::declval<__type72>())) __type73;
      typedef indexable<__type73> __type74;
      typedef typename __combined<__type26,__type74>::type __type75;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type77;
      typedef __type77 __type78;
      typedef decltype(std::declval<__type78>()[std::declval<__type54>()]) __type83;
      typedef typename pythonic::assignable<__type83>::type __type84;
      typedef __type84 __type85;
      typedef typename pythonic::assignable<__type2>::type __type86;
      typedef __type86 __type87;
      typedef decltype(pythonic::operator_::div(std::declval<__type85>(), std::declval<__type87>())) __type88;
      typedef decltype(std::declval<__type27>()(std::declval<__type88>())) __type89;
      typedef typename pythonic::assignable<__type89>::type __type90;
      typedef __type90 __type91;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type68>(), std::declval<__type91>())) __type92;
      typedef indexable<__type92> __type93;
      typedef typename __combined<__type75,__type93>::type __type94;
      typedef decltype(pythonic::operator_::add(std::declval<__type91>(), std::declval<__type64>())) __type97;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type68>(), std::declval<__type97>())) __type98;
      typedef indexable<__type98> __type99;
      typedef typename __combined<__type94,__type99>::type __type100;
      typedef decltype(std::declval<__type34>()[std::declval<__type54>()]) __type106;
      typedef typename pythonic::assignable<__type106>::type __type107;
      typedef __type107 __type108;
      typedef container<typename std::remove_reference<__type108>::type> __type109;
      typedef decltype(std::declval<__type20>()[std::declval<__type91>()]) __type113;
      typedef decltype(pythonic::operator_::sub(std::declval<__type85>(), std::declval<__type113>())) __type114;
      typedef decltype(pythonic::operator_::div(std::declval<__type114>(), std::declval<__type87>())) __type116;
      typedef typename pythonic::assignable<__type116>::type __type117;
      typedef __type117 __type118;
      typedef decltype(pythonic::operator_::sub(std::declval<__type64>(), std::declval<__type118>())) __type119;
      typedef decltype(pythonic::operator_::mul(std::declval<__type119>(), std::declval<__type108>())) __type121;
      typedef container<typename std::remove_reference<__type121>::type> __type122;
      typedef decltype(pythonic::operator_::mul(std::declval<__type118>(), std::declval<__type108>())) __type125;
      typedef container<typename std::remove_reference<__type125>::type> __type126;
      typedef typename __combined<__type100,__type74,__type109,__type93,__type122,__type99,__type126>::type __type127;
      typedef __type127 __type128;
      typedef typename pythonic::returnable<__type128>::type __type129;
      typedef __type3 __ptype30;
      typedef __type7 __ptype31;
      typedef __type129 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type operator()(argument_type0&& spectrum_k0k1k2, argument_type1&& khs, argument_type2&& KH, argument_type3&& kzs, argument_type4&& KZ) const
    ;
  }  ;
  struct loop_spectra3d
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type0;
      typedef __type0 __type1;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type1>::type>::type __type2;
      typedef __type2 __type3;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type4;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::len{})>::type>::type __type5;
      typedef std::integral_constant<long,1> __type6;
      typedef indexable_container<__type6, typename std::remove_reference<__type2>::type> __type7;
      typedef typename __combined<__type0,__type7>::type __type8;
      typedef __type8 __type9;
      typedef decltype(std::declval<__type5>()(std::declval<__type9>())) __type10;
      typedef typename pythonic::assignable<__type10>::type __type11;
      typedef __type11 __type12;
      typedef decltype(std::declval<__type4>()(std::declval<__type12>())) __type13;
      typedef typename pythonic::assignable<__type13>::type __type14;
      typedef long __type16;
      typedef decltype(pythonic::operator_::sub(std::declval<__type12>(), std::declval<__type16>())) __type17;
      typedef typename pythonic::lazy<__type17>::type __type18;
      typedef __type18 __type19;
      typedef indexable<__type19> __type20;
      typedef typename __combined<__type14,__type20>::type __type21;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::int_{})>::type>::type __type22;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sqrt{})>::type>::type __type23;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type24;
      typedef __type24 __type25;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type26;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type27;
      typedef __type27 __type28;
      typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type28>())) __type29;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type29>::type>::type __type30;
      typedef typename pythonic::lazy<__type30>::type __type31;
      typedef __type31 __type32;
      typedef decltype(std::declval<__type26>()(std::declval<__type32>())) __type33;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type33>::type::iterator>::value_type>::type __type34;
      typedef __type34 __type35;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type29>::type>::type __type36;
      typedef typename pythonic::lazy<__type36>::type __type37;
      typedef __type37 __type38;
      typedef decltype(std::declval<__type26>()(std::declval<__type38>())) __type39;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type39>::type::iterator>::value_type>::type __type40;
      typedef __type40 __type41;
      typedef typename std::tuple_element<2,typename std::remove_reference<__type29>::type>::type __type42;
      typedef typename pythonic::lazy<__type42>::type __type43;
      typedef __type43 __type44;
      typedef decltype(std::declval<__type26>()(std::declval<__type44>())) __type45;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type45>::type::iterator>::value_type>::type __type46;
      typedef __type46 __type47;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type35>(), std::declval<__type41>(), std::declval<__type47>())) __type48;
      typedef decltype(std::declval<__type25>()[std::declval<__type48>()]) __type49;
      typedef decltype(std::declval<__type23>()(std::declval<__type49>())) __type50;
      typedef typename pythonic::assignable<__type50>::type __type51;
      typedef __type51 __type52;
      typedef typename pythonic::assignable<__type2>::type __type53;
      typedef __type53 __type54;
      typedef decltype(pythonic::operator_::div(std::declval<__type52>(), std::declval<__type54>())) __type55;
      typedef decltype(std::declval<__type22>()(std::declval<__type55>())) __type56;
      typedef typename pythonic::assignable<__type56>::type __type57;
      typedef __type57 __type58;
      typedef indexable<__type58> __type59;
      typedef typename __combined<__type21,__type59>::type __type60;
      typedef decltype(pythonic::operator_::add(std::declval<__type58>(), std::declval<__type16>())) __type62;
      typedef indexable<__type62> __type63;
      typedef typename __combined<__type60,__type63>::type __type64;
      typedef decltype(std::declval<__type28>()[std::declval<__type48>()]) __type70;
      typedef typename pythonic::assignable<__type70>::type __type71;
      typedef __type71 __type72;
      typedef container<typename std::remove_reference<__type72>::type> __type73;
      typedef decltype(std::declval<__type9>()[std::declval<__type58>()]) __type77;
      typedef decltype(pythonic::operator_::sub(std::declval<__type52>(), std::declval<__type77>())) __type78;
      typedef decltype(pythonic::operator_::div(std::declval<__type78>(), std::declval<__type54>())) __type80;
      typedef typename pythonic::assignable<__type80>::type __type81;
      typedef __type81 __type82;
      typedef decltype(pythonic::operator_::sub(std::declval<__type16>(), std::declval<__type82>())) __type83;
      typedef decltype(pythonic::operator_::mul(std::declval<__type83>(), std::declval<__type72>())) __type85;
      typedef container<typename std::remove_reference<__type85>::type> __type86;
      typedef decltype(pythonic::operator_::mul(std::declval<__type82>(), std::declval<__type72>())) __type89;
      typedef container<typename std::remove_reference<__type89>::type> __type90;
      typedef typename __combined<__type64,__type20,__type73,__type59,__type86,__type63,__type90>::type __type91;
      typedef __type91 __type92;
      typedef typename pythonic::returnable<__type92>::type __type93;
      typedef __type3 __ptype32;
      typedef __type93 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    inline
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& spectrum_k0k1k2, argument_type1&& ks, argument_type2&& K2) const
    ;
  }  ;
  struct vector_product
  {
    typedef void callable;
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type0;
      typedef __type0 __type1;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type3;
      typedef __type3 __type4;
      typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type4>())) __type5;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type5>::type>::type __type6;
      typedef typename pythonic::lazy<__type6>::type __type7;
      typedef __type7 __type8;
      typedef decltype(std::declval<__type2>()(std::declval<__type8>())) __type9;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type __type10;
      typedef __type10 __type11;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type5>::type>::type __type12;
      typedef typename pythonic::lazy<__type12>::type __type13;
      typedef __type13 __type14;
      typedef decltype(std::declval<__type2>()(std::declval<__type14>())) __type15;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
      typedef __type16 __type17;
      typedef typename std::tuple_element<2,typename std::remove_reference<__type5>::type>::type __type18;
      typedef typename pythonic::lazy<__type18>::type __type19;
      typedef __type19 __type20;
      typedef decltype(std::declval<__type2>()(std::declval<__type20>())) __type21;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type21>::type::iterator>::value_type>::type __type22;
      typedef __type22 __type23;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type11>(), std::declval<__type17>(), std::declval<__type23>())) __type24;
      typedef decltype(std::declval<__type1>()[std::declval<__type24>()]) __type25;
      typedef typename pythonic::assignable<__type25>::type __type26;
      typedef __type26 __type27;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type28;
      typedef decltype(std::declval<__type4>()[std::declval<__type24>()]) __type34;
      typedef typename pythonic::assignable<__type34>::type __type35;
      typedef __type35 __type36;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type37;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type38;
      typedef __type38 __type39;
      typedef decltype(std::declval<__type39>()[std::declval<__type24>()]) __type44;
      typedef typename pythonic::assignable<__type44>::type __type45;
      typedef __type45 __type46;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type47;
      typedef __type28 __type48;
      typedef decltype(std::declval<__type48>()[std::declval<__type24>()]) __type53;
      typedef typename pythonic::assignable<__type53>::type __type54;
      typedef __type54 __type55;
      typedef decltype(pythonic::operator_::mul(std::declval<__type27>(), std::declval<__type55>())) __type56;
      typedef __type37 __type58;
      typedef decltype(std::declval<__type58>()[std::declval<__type24>()]) __type63;
      typedef typename pythonic::assignable<__type63>::type __type64;
      typedef __type64 __type65;
      typedef decltype(pythonic::operator_::mul(std::declval<__type46>(), std::declval<__type65>())) __type66;
      typedef decltype(pythonic::operator_::sub(std::declval<__type56>(), std::declval<__type66>())) __type67;
      typedef container<typename std::remove_reference<__type67>::type> __type68;
      typedef indexable<__type24> __type73;
      typedef typename __combined<__type47,__type68,__type73>::type __type74;
      typedef __type74 __type75;
      typedef decltype(std::declval<__type75>()[std::declval<__type24>()]) __type80;
      typedef typename pythonic::assignable<__type80>::type __type81;
      typedef __type81 __type82;
      typedef decltype(pythonic::operator_::mul(std::declval<__type46>(), std::declval<__type82>())) __type83;
      typedef decltype(pythonic::operator_::mul(std::declval<__type36>(), std::declval<__type55>())) __type86;
      typedef decltype(pythonic::operator_::sub(std::declval<__type83>(), std::declval<__type86>())) __type87;
      typedef container<typename std::remove_reference<__type87>::type> __type88;
      typedef typename __combined<__type37,__type88,__type73>::type __type94;
      typedef decltype(pythonic::operator_::mul(std::declval<__type36>(), std::declval<__type65>())) __type96;
      typedef decltype(pythonic::operator_::mul(std::declval<__type27>(), std::declval<__type82>())) __type99;
      typedef decltype(pythonic::operator_::sub(std::declval<__type96>(), std::declval<__type99>())) __type100;
      typedef container<typename std::remove_reference<__type100>::type> __type101;
      typedef typename __combined<__type28,__type101,__type73>::type __type107;
      typedef __type67 __type108;
      typedef __type24 __type109;
      typedef __type94 __type111;
      typedef __type107 __type112;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type75>(), std::declval<__type111>(), std::declval<__type112>())) __type113;
      typedef typename pythonic::returnable<__type113>::type __type114;
      typedef __type108 __ptype33;
      typedef __type109 __ptype34;
      typedef __type114 result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
    inline
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type operator()(argument_type0&& ax, argument_type1&& ay, argument_type2&& az, argument_type3&& bx, argument_type4&& by, argument_type5&& bz) const
    ;
  }  ;
  inline
  typename __transonic__::type::result_type __transonic__::operator()() const
  {
    {
      static typename __transonic__::type::result_type tmp_global = pythonic::types::make_tuple(pythonic::types::str("0.5.0"));
      return tmp_global;
    }
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::type::result_type __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft):\n    return backend_func(self.Kx, self.Ky, vx_fft, vy_fft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::type<argument_type0, argument_type1, argument_type2, argument_type3>::result_type __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& vx_fft, argument_type3&& vy_fft) const
  {
    return pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Kx, vy_fft), pythonic::operator_::mul(self_Ky, vx_fft)));
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::type::result_type __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft, vz_fft, rotxfft, rotyfft, rotzfft):\n    return backend_func(self.Kx, self.Ky, self.Kz, vx_fft, vy_fft, vz_fft, rotxfft, rotyfft, rotzfft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 , typename argument_type7 , typename argument_type8 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6, argument_type7, argument_type8>::result_type __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft, argument_type6&& rotxfft, argument_type7&& rotyfft, argument_type8&& rotzfft) const
  {
    typename pythonic::lazy<decltype(std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n0 = std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    typename pythonic::lazy<decltype(std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n1 = std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    typename pythonic::lazy<decltype(std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n2 = std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    {
      long  __target139945938599024 = n0;
      for (long  i0=0L; i0 < __target139945938599024; i0 += 1L)
      {
        {
          long  __target139945938673872 = n1;
          for (long  i1=0L; i1 < __target139945938673872; i1 += 1L)
          {
            {
              long  __target139945938674448 = n2;
              for (long  i2=0L; i2 < __target139945938674448; i2 += 1L)
              {
                rotxfft.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Ky.fast(pythonic::types::make_tuple(i0, i1, i2)), vz_fft.fast(pythonic::types::make_tuple(i0, i1, i2))), pythonic::operator_::mul(self_Kz.fast(pythonic::types::make_tuple(i0, i1, i2)), vy_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))));
                rotyfft.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Kz.fast(pythonic::types::make_tuple(i0, i1, i2)), vx_fft.fast(pythonic::types::make_tuple(i0, i1, i2))), pythonic::operator_::mul(self_Kx.fast(pythonic::types::make_tuple(i0, i1, i2)), vz_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))));
                rotzfft.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Kx.fast(pythonic::types::make_tuple(i0, i1, i2)), vy_fft.fast(pythonic::types::make_tuple(i0, i1, i2))), pythonic::operator_::mul(self_Ky.fast(pythonic::types::make_tuple(i0, i1, i2)), vx_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))));
              }
            }
          }
        }
      }
    }
    return pythonic::builtins::None;
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::type::result_type __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft, vz_fft):\n    return backend_func(self.Kx, self.Ky, self.Kz, vx_fft, vy_fft, vz_fft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft) const
  {
    return pythonic::types::make_tuple(pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Ky, vz_fft), pythonic::operator_::mul(self_Kz, vy_fft))), pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Kz, vx_fft), pythonic::operator_::mul(self_Kx, vz_fft))), pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::sub(pythonic::operator_::mul(self_Kx, vy_fft), pythonic::operator_::mul(self_Ky, vx_fft))));
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::type::result_type __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft, vz_fft):\n    return backend_func(self.Kx, self.Ky, self.Kz, vx_fft, vy_fft, vz_fft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& vx_fft, argument_type4&& vy_fft, argument_type5&& vz_fft) const
  {
    return pythonic::operator_::mul(std::complex<double>(0.0, 1.0), pythonic::operator_::add(pythonic::operator_::add(pythonic::operator_::mul(self_Kx, vx_fft), pythonic::operator_::mul(self_Ky, vy_fft)), pythonic::operator_::mul(self_Kz, vz_fft)));
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d::type::result_type __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft, vz_fft):\n    return backend_func(self.Kx, self.Ky, self.Kz, self.inv_K_square_nozero, vx_fft, vy_fft, vz_fft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__project_perpk3d::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& self_inv_K_square_nozero, argument_type4&& vx_fft, argument_type5&& vy_fft, argument_type6&& vz_fft) const
  {
    typename pythonic::lazy<decltype(std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n0 = std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    typename pythonic::lazy<decltype(std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n1 = std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    typename pythonic::lazy<decltype(std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft)))>::type n2 = std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, vx_fft));
    {
      long  __target139946008061120 = n0;
      for (long  i0=0L; i0 < __target139946008061120; i0 += 1L)
      {
        {
          long  __target139946008062176 = n1;
          for (long  i1=0L; i1 < __target139946008062176; i1 += 1L)
          {
            {
              long  __target139946008062752 = n2;
              for (long  i2=0L; i2 < __target139946008062752; i2 += 1L)
              {
                typename pythonic::assignable_noescape<decltype(pythonic::operator_::mul(pythonic::operator_::add(pythonic::operator_::add(pythonic::operator_::mul(self_Kx.fast(pythonic::types::make_tuple(i0, i1, i2)), vx_fft.fast(pythonic::types::make_tuple(i0, i1, i2))), pythonic::operator_::mul(self_Ky.fast(pythonic::types::make_tuple(i0, i1, i2)), vy_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))), pythonic::operator_::mul(self_Kz.fast(pythonic::types::make_tuple(i0, i1, i2)), vz_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))), self_inv_K_square_nozero.fast(pythonic::types::make_tuple(i0, i1, i2))))>::type tmp = pythonic::operator_::mul(pythonic::operator_::add(pythonic::operator_::add(pythonic::operator_::mul(self_Kx.fast(pythonic::types::make_tuple(i0, i1, i2)), vx_fft.fast(pythonic::types::make_tuple(i0, i1, i2))), pythonic::operator_::mul(self_Ky.fast(pythonic::types::make_tuple(i0, i1, i2)), vy_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))), pythonic::operator_::mul(self_Kz.fast(pythonic::types::make_tuple(i0, i1, i2)), vz_fft.fast(pythonic::types::make_tuple(i0, i1, i2)))), self_inv_K_square_nozero.fast(pythonic::types::make_tuple(i0, i1, i2)));
                vx_fft.fast(pythonic::types::make_tuple(i0, i1, i2)) -= pythonic::operator_::mul(self_Kx.fast(pythonic::types::make_tuple(i0, i1, i2)), tmp);
                vy_fft.fast(pythonic::types::make_tuple(i0, i1, i2)) -= pythonic::operator_::mul(self_Ky.fast(pythonic::types::make_tuple(i0, i1, i2)), tmp);
                vz_fft.fast(pythonic::types::make_tuple(i0, i1, i2)) -= pythonic::operator_::mul(self_Kz.fast(pythonic::types::make_tuple(i0, i1, i2)), tmp);
              }
            }
          }
        }
      }
    }
    return pythonic::builtins::None;
  }
  inline
  typename __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::type::result_type __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::operator()() const
  {
    {
      static typename __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::type::result_type tmp_global = pythonic::types::str("\n\ndef new_method(self, vx_fft, vy_fft, vz_fft):\n    return backend_func(self.Kx, self.Ky, self.Kz, self.inv_K_square_nozero, vx_fft, vy_fft, vz_fft)\n\n");
      return tmp_global;
    }
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 , typename argument_type6 >
  inline
  typename __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5, argument_type6>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::operator()(argument_type0&& self_Kx, argument_type1&& self_Ky, argument_type2&& self_Kz, argument_type3&& self_inv_K_square_nozero, argument_type4&& vx_fft, argument_type5&& vy_fft, argument_type6&& vz_fft) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<argument_type6>::type>::type __type0;
    typedef __type0 __type1;
    typedef typename pythonic::assignable<__type1>::type __type2;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type3;
    typedef __type3 __type4;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type5;
    typedef __type5 __type6;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type7;
    typedef __type7 __type8;
    typedef typename pythonic::assignable<__type8>::type __type9;
    typedef __type9 __type11;
    typedef decltype(pythonic::operator_::mul(std::declval<__type6>(), std::declval<__type11>())) __type12;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type13;
    typedef __type13 __type14;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type5>::type>::type __type15;
    typedef __type15 __type16;
    typedef typename pythonic::assignable<__type16>::type __type17;
    typedef __type17 __type19;
    typedef decltype(pythonic::operator_::mul(std::declval<__type14>(), std::declval<__type19>())) __type20;
    typedef decltype(pythonic::operator_::add(std::declval<__type12>(), std::declval<__type20>())) __type21;
    typedef __type2 __type23;
    typedef decltype(pythonic::operator_::mul(std::declval<__type4>(), std::declval<__type23>())) __type24;
    typedef decltype(pythonic::operator_::add(std::declval<__type21>(), std::declval<__type24>())) __type25;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type26;
    typedef __type26 __type27;
    typedef decltype(pythonic::operator_::mul(std::declval<__type25>(), std::declval<__type27>())) __type28;
    typedef typename pythonic::assignable<__type28>::type __type29;
    typedef __type29 __type30;
    typedef decltype(pythonic::operator_::mul(std::declval<__type4>(), std::declval<__type30>())) __type31;
    typedef typename __combined<__type2,__type31>::type __type32;
    typedef decltype(pythonic::operator_::mul(std::declval<__type14>(), std::declval<__type30>())) __type34;
    typedef typename __combined<__type17,__type34>::type __type35;
    typedef decltype(pythonic::operator_::mul(std::declval<__type6>(), std::declval<__type30>())) __type37;
    typedef typename __combined<__type9,__type37>::type __type38;
    typedef typename pythonic::assignable<__type32>::type __type39;
    typedef typename pythonic::assignable<__type35>::type __type40;
    typedef typename pythonic::assignable<__type38>::type __type41;
    __type39 vz_fft_ = vz_fft;
    __type40 vy_fft_ = vy_fft;
    __type41 vx_fft_ = vx_fft;
    typename pythonic::assignable_noescape<decltype(pythonic::operator_::mul(pythonic::operator_::add(pythonic::operator_::add(pythonic::operator_::mul(self_Kx, vx_fft_), pythonic::operator_::mul(self_Ky, vy_fft_)), pythonic::operator_::mul(self_Kz, vz_fft_)), self_inv_K_square_nozero))>::type tmp = pythonic::operator_::mul(pythonic::operator_::add(pythonic::operator_::add(pythonic::operator_::mul(self_Kx, vx_fft_), pythonic::operator_::mul(self_Ky, vy_fft_)), pythonic::operator_::mul(self_Kz, vz_fft_)), self_inv_K_square_nozero);
    vx_fft_ -= pythonic::operator_::mul(self_Kx, tmp);
    vy_fft_ -= pythonic::operator_::mul(self_Ky, tmp);
    vz_fft_ -= pythonic::operator_::mul(self_Kz, tmp);
    return pythonic::builtins::None;
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
  inline
  typename loop_spectra_kzkh::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type loop_spectra_kzkh::operator()(argument_type0&& spectrum_k0k1k2, argument_type1&& khs, argument_type2&& KH, argument_type3&& kzs, argument_type4&& KZ) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::pythran::functor::make_shape{})>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::len{})>::type>::type __type2;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type3;
    typedef std::integral_constant<long,1> __type4;
    typedef __type3 __type5;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type5>::type>::type __type6;
    typedef indexable_container<__type4, typename std::remove_reference<__type6>::type> __type7;
    typedef typename __combined<__type3,__type7>::type __type8;
    typedef __type8 __type9;
    typedef decltype(std::declval<__type2>()(std::declval<__type9>())) __type10;
    typedef typename pythonic::assignable<__type10>::type __type11;
    typedef __type11 __type12;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type13;
    typedef __type13 __type14;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type14>::type>::type __type15;
    typedef indexable_container<__type4, typename std::remove_reference<__type15>::type> __type16;
    typedef typename __combined<__type13,__type16>::type __type17;
    typedef __type17 __type18;
    typedef decltype(std::declval<__type2>()(std::declval<__type18>())) __type19;
    typedef typename pythonic::assignable<__type19>::type __type20;
    typedef __type20 __type21;
    typedef decltype(std::declval<__type1>()(std::declval<__type12>(), std::declval<__type21>())) __type22;
    typedef decltype(std::declval<__type0>()(std::declval<__type22>())) __type23;
    typedef typename pythonic::assignable<__type23>::type __type24;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::int_{})>::type>::type __type25;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::round{})>::type>::type __type26;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::abs{})>::type>::type __type27;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type28;
    typedef __type28 __type29;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type30;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type31;
    typedef __type31 __type32;
    typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type32>())) __type33;
    typedef typename std::tuple_element<0,typename std::remove_reference<__type33>::type>::type __type34;
    typedef typename pythonic::lazy<__type34>::type __type35;
    typedef __type35 __type36;
    typedef decltype(std::declval<__type30>()(std::declval<__type36>())) __type37;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type37>::type::iterator>::value_type>::type __type38;
    typedef __type38 __type39;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type33>::type>::type __type40;
    typedef typename pythonic::lazy<__type40>::type __type41;
    typedef __type41 __type42;
    typedef decltype(std::declval<__type30>()(std::declval<__type42>())) __type43;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type43>::type::iterator>::value_type>::type __type44;
    typedef __type44 __type45;
    typedef typename std::tuple_element<2,typename std::remove_reference<__type33>::type>::type __type46;
    typedef typename pythonic::lazy<__type46>::type __type47;
    typedef __type47 __type48;
    typedef decltype(std::declval<__type30>()(std::declval<__type48>())) __type49;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type49>::type::iterator>::value_type>::type __type50;
    typedef __type50 __type51;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type39>(), std::declval<__type45>(), std::declval<__type51>())) __type52;
    typedef decltype(std::declval<__type29>()[std::declval<__type52>()]) __type53;
    typedef decltype(std::declval<__type27>()(std::declval<__type53>())) __type54;
    typedef typename pythonic::assignable<__type6>::type __type55;
    typedef __type55 __type56;
    typedef decltype(pythonic::operator_::div(std::declval<__type54>(), std::declval<__type56>())) __type57;
    typedef decltype(std::declval<__type26>()(std::declval<__type57>())) __type58;
    typedef decltype(std::declval<__type25>()(std::declval<__type58>())) __type59;
    typedef typename pythonic::lazy<__type59>::type __type60;
    typedef long __type62;
    typedef decltype(pythonic::operator_::sub(std::declval<__type12>(), std::declval<__type62>())) __type63;
    typedef typename pythonic::lazy<__type63>::type __type64;
    typedef typename __combined<__type60,__type64>::type __type65;
    typedef __type65 __type66;
    typedef decltype(pythonic::operator_::sub(std::declval<__type21>(), std::declval<__type62>())) __type68;
    typedef typename pythonic::lazy<__type68>::type __type69;
    typedef __type69 __type70;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type66>(), std::declval<__type70>())) __type71;
    typedef indexable<__type71> __type72;
    typedef typename __combined<__type24,__type72>::type __type73;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type75;
    typedef __type75 __type76;
    typedef decltype(std::declval<__type76>()[std::declval<__type52>()]) __type81;
    typedef typename pythonic::assignable<__type81>::type __type82;
    typedef __type82 __type83;
    typedef typename pythonic::assignable<__type15>::type __type84;
    typedef __type84 __type85;
    typedef decltype(pythonic::operator_::div(std::declval<__type83>(), std::declval<__type85>())) __type86;
    typedef decltype(std::declval<__type25>()(std::declval<__type86>())) __type87;
    typedef typename pythonic::assignable<__type87>::type __type88;
    typedef __type88 __type89;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type66>(), std::declval<__type89>())) __type90;
    typedef indexable<__type90> __type91;
    typedef typename __combined<__type73,__type91>::type __type92;
    typedef decltype(pythonic::operator_::add(std::declval<__type89>(), std::declval<__type62>())) __type95;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type66>(), std::declval<__type95>())) __type96;
    typedef indexable<__type96> __type97;
    typedef typename __combined<__type92,__type97>::type __type98;
    typedef decltype(std::declval<__type32>()[std::declval<__type52>()]) __type104;
    typedef typename pythonic::assignable<__type104>::type __type105;
    typedef __type105 __type106;
    typedef container<typename std::remove_reference<__type106>::type> __type107;
    typedef decltype(std::declval<__type18>()[std::declval<__type89>()]) __type111;
    typedef decltype(pythonic::operator_::sub(std::declval<__type83>(), std::declval<__type111>())) __type112;
    typedef decltype(pythonic::operator_::div(std::declval<__type112>(), std::declval<__type85>())) __type114;
    typedef typename pythonic::assignable<__type114>::type __type115;
    typedef __type115 __type116;
    typedef decltype(pythonic::operator_::sub(std::declval<__type62>(), std::declval<__type116>())) __type117;
    typedef decltype(pythonic::operator_::mul(std::declval<__type117>(), std::declval<__type106>())) __type119;
    typedef container<typename std::remove_reference<__type119>::type> __type120;
    typedef decltype(pythonic::operator_::mul(std::declval<__type116>(), std::declval<__type106>())) __type123;
    typedef container<typename std::remove_reference<__type123>::type> __type124;
    typedef typename __combined<__type98,__type72,__type107,__type91,__type120,__type97,__type124>::type __type125;
    typedef typename pythonic::assignable<__type125>::type __type126;
    typedef typename pythonic::lazy<__type65>::type __type127;
    typedef typename pythonic::assignable<__type115>::type __type128;
    typename pythonic::assignable_noescape<decltype(std::get<1>(khs))>::type deltakh = std::get<1>(khs);
    typename pythonic::assignable_noescape<decltype(std::get<1>(kzs))>::type deltakz = std::get<1>(kzs);
    typename pythonic::assignable_noescape<decltype(pythonic::builtins::functor::len{}(khs))>::type nkh = pythonic::builtins::functor::len{}(khs);
    typename pythonic::assignable_noescape<decltype(pythonic::builtins::functor::len{}(kzs))>::type nkz = pythonic::builtins::functor::len{}(kzs);
    __type126 spectrum_kzkh = pythonic::numpy::functor::zeros{}(pythonic::builtins::pythran::functor::make_shape{}(nkz, nkh));
    typename pythonic::lazy<decltype(std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk0 = std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    typename pythonic::lazy<decltype(std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk1 = std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    typename pythonic::lazy<decltype(std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk2 = std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    {
      long  __target139946007855792 = nk0;
      for (long  ik0=0L; ik0 < __target139946007855792; ik0 += 1L)
      {
        {
          long  __target139946007857856 = nk1;
          for (long  ik1=0L; ik1 < __target139946007857856; ik1 += 1L)
          {
            {
              long  __target139946007858432 = nk2;
              for (long  ik2=0L; ik2 < __target139946007858432; ik2 += 1L)
              {
                typename pythonic::assignable_noescape<decltype(spectrum_k0k1k2[pythonic::types::make_tuple(ik0, ik1, ik2)])>::type value = spectrum_k0k1k2[pythonic::types::make_tuple(ik0, ik1, ik2)];
                typename pythonic::assignable_noescape<decltype(KH[pythonic::types::make_tuple(ik0, ik1, ik2)])>::type kappa = KH[pythonic::types::make_tuple(ik0, ik1, ik2)];
                typename pythonic::assignable_noescape<decltype(pythonic::builtins::functor::int_{}(pythonic::operator_::div(kappa, deltakh)))>::type ikh = pythonic::builtins::functor::int_{}(pythonic::operator_::div(kappa, deltakh));
                __type127 ikz = pythonic::builtins::functor::int_{}(pythonic::builtins::functor::round{}(pythonic::operator_::div(pythonic::builtins::functor::abs{}(KZ[pythonic::types::make_tuple(ik0, ik1, ik2)]), deltakz)));
                if (pythonic::operator_::ge(ikz, pythonic::operator_::sub(nkz, 1L)))
                {
                  ikz = pythonic::operator_::sub(nkz, 1L);
                }
                {
                  __type128 coef_share;
                  if (pythonic::operator_::ge(ikh, pythonic::operator_::sub(nkh, 1L)))
                  {
                    typename pythonic::lazy<decltype(pythonic::operator_::sub(nkh, 1L))>::type ikh_ = pythonic::operator_::sub(nkh, 1L);
                    spectrum_kzkh[pythonic::types::make_tuple(ikz, ikh_)] += value;
                  }
                  else
                  {
                    coef_share = pythonic::operator_::div(pythonic::operator_::sub(kappa, khs[ikh]), deltakh);
                    spectrum_kzkh[pythonic::types::make_tuple(ikz, ikh)] += pythonic::operator_::mul(pythonic::operator_::sub(1L, coef_share), value);
                    spectrum_kzkh[pythonic::types::make_tuple(ikz, pythonic::operator_::add(ikh, 1L))] += pythonic::operator_::mul(coef_share, value);
                  }
                }
              }
            }
          }
        }
      }
    }
    return spectrum_kzkh;
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  inline
  typename loop_spectra3d::type<argument_type0, argument_type1, argument_type2>::result_type loop_spectra3d::operator()(argument_type0&& spectrum_k0k1k2, argument_type1&& ks, argument_type2&& K2) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::len{})>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type2;
    typedef std::integral_constant<long,1> __type3;
    typedef __type2 __type4;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type4>::type>::type __type5;
    typedef indexable_container<__type3, typename std::remove_reference<__type5>::type> __type6;
    typedef typename __combined<__type2,__type6>::type __type7;
    typedef __type7 __type8;
    typedef decltype(std::declval<__type1>()(std::declval<__type8>())) __type9;
    typedef typename pythonic::assignable<__type9>::type __type10;
    typedef __type10 __type11;
    typedef decltype(std::declval<__type0>()(std::declval<__type11>())) __type12;
    typedef typename pythonic::assignable<__type12>::type __type13;
    typedef long __type15;
    typedef decltype(pythonic::operator_::sub(std::declval<__type11>(), std::declval<__type15>())) __type16;
    typedef typename pythonic::lazy<__type16>::type __type17;
    typedef __type17 __type18;
    typedef indexable<__type18> __type19;
    typedef typename __combined<__type13,__type19>::type __type20;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::int_{})>::type>::type __type21;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sqrt{})>::type>::type __type22;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type23;
    typedef __type23 __type24;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::builtins::functor::range{})>::type>::type __type25;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type26;
    typedef __type26 __type27;
    typedef decltype(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type27>())) __type28;
    typedef typename std::tuple_element<0,typename std::remove_reference<__type28>::type>::type __type29;
    typedef typename pythonic::lazy<__type29>::type __type30;
    typedef __type30 __type31;
    typedef decltype(std::declval<__type25>()(std::declval<__type31>())) __type32;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type32>::type::iterator>::value_type>::type __type33;
    typedef __type33 __type34;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type28>::type>::type __type35;
    typedef typename pythonic::lazy<__type35>::type __type36;
    typedef __type36 __type37;
    typedef decltype(std::declval<__type25>()(std::declval<__type37>())) __type38;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type38>::type::iterator>::value_type>::type __type39;
    typedef __type39 __type40;
    typedef typename std::tuple_element<2,typename std::remove_reference<__type28>::type>::type __type41;
    typedef typename pythonic::lazy<__type41>::type __type42;
    typedef __type42 __type43;
    typedef decltype(std::declval<__type25>()(std::declval<__type43>())) __type44;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type44>::type::iterator>::value_type>::type __type45;
    typedef __type45 __type46;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type34>(), std::declval<__type40>(), std::declval<__type46>())) __type47;
    typedef decltype(std::declval<__type24>()[std::declval<__type47>()]) __type48;
    typedef decltype(std::declval<__type22>()(std::declval<__type48>())) __type49;
    typedef typename pythonic::assignable<__type49>::type __type50;
    typedef __type50 __type51;
    typedef typename pythonic::assignable<__type5>::type __type52;
    typedef __type52 __type53;
    typedef decltype(pythonic::operator_::div(std::declval<__type51>(), std::declval<__type53>())) __type54;
    typedef decltype(std::declval<__type21>()(std::declval<__type54>())) __type55;
    typedef typename pythonic::assignable<__type55>::type __type56;
    typedef __type56 __type57;
    typedef indexable<__type57> __type58;
    typedef typename __combined<__type20,__type58>::type __type59;
    typedef decltype(pythonic::operator_::add(std::declval<__type57>(), std::declval<__type15>())) __type61;
    typedef indexable<__type61> __type62;
    typedef typename __combined<__type59,__type62>::type __type63;
    typedef decltype(std::declval<__type27>()[std::declval<__type47>()]) __type69;
    typedef typename pythonic::assignable<__type69>::type __type70;
    typedef __type70 __type71;
    typedef container<typename std::remove_reference<__type71>::type> __type72;
    typedef decltype(std::declval<__type8>()[std::declval<__type57>()]) __type76;
    typedef decltype(pythonic::operator_::sub(std::declval<__type51>(), std::declval<__type76>())) __type77;
    typedef decltype(pythonic::operator_::div(std::declval<__type77>(), std::declval<__type53>())) __type79;
    typedef typename pythonic::assignable<__type79>::type __type80;
    typedef __type80 __type81;
    typedef decltype(pythonic::operator_::sub(std::declval<__type15>(), std::declval<__type81>())) __type82;
    typedef decltype(pythonic::operator_::mul(std::declval<__type82>(), std::declval<__type71>())) __type84;
    typedef container<typename std::remove_reference<__type84>::type> __type85;
    typedef decltype(pythonic::operator_::mul(std::declval<__type81>(), std::declval<__type71>())) __type88;
    typedef container<typename std::remove_reference<__type88>::type> __type89;
    typedef typename __combined<__type63,__type19,__type72,__type58,__type85,__type62,__type89>::type __type90;
    typedef typename pythonic::assignable<__type90>::type __type91;
    typedef typename pythonic::assignable<__type80>::type __type92;
    typename pythonic::assignable_noescape<decltype(std::get<1>(ks))>::type deltak = std::get<1>(ks);
    typename pythonic::assignable_noescape<decltype(pythonic::builtins::functor::len{}(ks))>::type nk = pythonic::builtins::functor::len{}(ks);
    __type91 spectrum3d = pythonic::numpy::functor::zeros{}(nk);
    typename pythonic::lazy<decltype(std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk0 = std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    typename pythonic::lazy<decltype(std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk1 = std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    typename pythonic::lazy<decltype(std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2)))>::type nk2 = std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, spectrum_k0k1k2));
    {
      long  __target139946007480832 = nk0;
      for (long  ik0=0L; ik0 < __target139946007480832; ik0 += 1L)
      {
        {
          long  __target139946007466288 = nk1;
          for (long  ik1=0L; ik1 < __target139946007466288; ik1 += 1L)
          {
            {
              long  __target139946007466864 = nk2;
              for (long  ik2=0L; ik2 < __target139946007466864; ik2 += 1L)
              {
                typename pythonic::assignable_noescape<decltype(spectrum_k0k1k2[pythonic::types::make_tuple(ik0, ik1, ik2)])>::type value = spectrum_k0k1k2[pythonic::types::make_tuple(ik0, ik1, ik2)];
                typename pythonic::assignable_noescape<decltype(pythonic::numpy::functor::sqrt{}(K2[pythonic::types::make_tuple(ik0, ik1, ik2)]))>::type kappa = pythonic::numpy::functor::sqrt{}(K2[pythonic::types::make_tuple(ik0, ik1, ik2)]);
                typename pythonic::assignable_noescape<decltype(pythonic::builtins::functor::int_{}(pythonic::operator_::div(kappa, deltak)))>::type ik = pythonic::builtins::functor::int_{}(pythonic::operator_::div(kappa, deltak));
                {
                  __type92 coef_share;
                  if (pythonic::operator_::ge(ik, pythonic::operator_::sub(nk, 1L)))
                  {
                    typename pythonic::lazy<decltype(pythonic::operator_::sub(nk, 1L))>::type ik_ = pythonic::operator_::sub(nk, 1L);
                    spectrum3d[ik_] += value;
                  }
                  else
                  {
                    coef_share = pythonic::operator_::div(pythonic::operator_::sub(kappa, ks[ik]), deltak);
                    spectrum3d[ik] += pythonic::operator_::mul(pythonic::operator_::sub(1L, coef_share), value);
                    spectrum3d[pythonic::operator_::add(ik, 1L)] += pythonic::operator_::mul(coef_share, value);
                  }
                }
              }
            }
          }
        }
      }
    }
    return spectrum3d;
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 , typename argument_type5 >
  inline
  typename vector_product::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4, argument_type5>::result_type vector_product::operator()(argument_type0&& ax, argument_type1&& ay, argument_type2&& az, argument_type3&& bx, argument_type4&& by, argument_type5&& bz) const
  {
    typename pythonic::lazy<decltype(std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax)))>::type n0 = std::get<0>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax));
    typename pythonic::lazy<decltype(std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax)))>::type n1 = std::get<1>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax));
    typename pythonic::lazy<decltype(std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax)))>::type n2 = std::get<2>(pythonic::builtins::getattr(pythonic::types::attr::SHAPE{}, ax));
    {
      long  __target139946010556016 = n0;
      for (long  i0=0L; i0 < __target139946010556016; i0 += 1L)
      {
        {
          long  __target139946007630608 = n1;
          for (long  i1=0L; i1 < __target139946007630608; i1 += 1L)
          {
            {
              long  __target139945937300976 = n2;
              for (long  i2=0L; i2 < __target139945937300976; i2 += 1L)
              {
                typename pythonic::assignable_noescape<decltype(ax.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_ax = ax.fast(pythonic::types::make_tuple(i0, i1, i2));
                typename pythonic::assignable_noescape<decltype(ay.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_ay = ay.fast(pythonic::types::make_tuple(i0, i1, i2));
                typename pythonic::assignable_noescape<decltype(az.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_az = az.fast(pythonic::types::make_tuple(i0, i1, i2));
                typename pythonic::assignable_noescape<decltype(bx.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_bx = bx.fast(pythonic::types::make_tuple(i0, i1, i2));
                typename pythonic::assignable_noescape<decltype(by.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_by = by.fast(pythonic::types::make_tuple(i0, i1, i2));
                typename pythonic::assignable_noescape<decltype(bz.fast(pythonic::types::make_tuple(i0, i1, i2)))>::type elem_bz = bz.fast(pythonic::types::make_tuple(i0, i1, i2));
                bx.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::sub(pythonic::operator_::mul(elem_ay, elem_bz), pythonic::operator_::mul(elem_az, elem_by));
                by.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::sub(pythonic::operator_::mul(elem_az, elem_bx), pythonic::operator_::mul(elem_ax, elem_bz));
                bz.fast(pythonic::types::make_tuple(i0, i1, i2)) = pythonic::operator_::sub(pythonic::operator_::mul(elem_ax, elem_by), pythonic::operator_::mul(elem_ay, elem_bx));
              }
            }
          }
        }
      }
    }
    return pythonic::types::make_tuple(bx, by, bz);
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
static PyObject* __transonic__ = to_python(__pythran_operators::__transonic__()());
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft()(self_Kx, self_Ky, vx_fft, vy_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vz_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& rotxfft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& rotyfft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& rotzfft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin()(self_Kx, self_Ky, self_Kz, vx_fft, vy_fft, vz_fft, rotxfft, rotyfft, rotzfft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft()(self_Kx, self_Ky, self_Kz, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft()(self_Kx, self_Ky, self_Kz, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__project_perpk3d()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_inv_K_square_nozero, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d()(self_Kx, self_Ky, self_Kz, self_inv_K_square_nozero, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d1(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_inv_K_square_nozero, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d()(self_Kx, self_Ky, self_Kz, self_inv_K_square_nozero, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
static PyObject* __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop = to_python(__pythran_operators::__code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop()());
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_inv_K_square_nozero, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop()(self_Kx, self_Ky, self_Kz, self_inv_K_square_nozero, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
inline
typename __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>::result_type __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop1(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Ky, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_Kz, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& self_inv_K_square_nozero, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vx_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vy_fft, pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>&& vz_fft) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop()(self_Kx, self_Ky, self_Kz, self_inv_K_square_nozero, vx_fft, vy_fft, vz_fft);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
inline
typename __pythran_operators::loop_spectra_kzkh::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>::result_type loop_spectra_kzkh0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& spectrum_k0k1k2, pythonic::types::ndarray<double,pythonic::types::pshape<long>>&& khs, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& KH, pythonic::types::ndarray<double,pythonic::types::pshape<long>>&& kzs, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& KZ) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::loop_spectra_kzkh()(spectrum_k0k1k2, khs, KH, kzs, KZ);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
inline
typename __pythran_operators::loop_spectra3d::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>::result_type loop_spectra3d0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& spectrum_k0k1k2, pythonic::types::ndarray<double,pythonic::types::pshape<long>>&& ks, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& K2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::loop_spectra3d()(spectrum_k0k1k2, ks, K2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
inline
typename __pythran_operators::vector_product::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>::result_type vector_product0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& ax, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& ay, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& az, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& bx, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& by, pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>&& bz) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_operators::vector_product()(ax, ay, az, bx, by, bz);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[4+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "vx_fft", "vy_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[9+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "vx_fft", "vy_fft", "vz_fft", "rotxfft", "rotyfft", "rotzfft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5], &args_obj[6], &args_obj[7], &args_obj[8]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[7]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[8]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[7]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[8])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[6+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[6+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[7+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "self_inv_K_square_nozero", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5], &args_obj[6]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[6]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__project_perpk3d0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[6])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[7+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "self_inv_K_square_nozero", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5], &args_obj[6]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__project_perpk3d1(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[7+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "self_inv_K_square_nozero", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5], &args_obj[6]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[6]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[6])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[7+1];
    
    char const* keywords[] = {"self_Kx", "self_Ky", "self_Kz", "self_inv_K_square_nozero", "vx_fft", "vy_fft", "vz_fft",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5], &args_obj[6]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]) && is_convertible<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6]))
        return to_python(__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop1(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[5]), from_python<pythonic::types::ndarray<std::complex<double>,pythonic::types::pshape<long,long,long>>>(args_obj[6])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_loop_spectra_kzkh0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[5+1];
    
    char const* keywords[] = {"spectrum_k0k1k2", "khs", "KH", "kzs", "KZ",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]))
        return to_python(loop_spectra_kzkh0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[3]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_loop_spectra3d0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    
    char const* keywords[] = {"spectrum_k0k1k2", "ks", "K2",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]))
        return to_python(loop_spectra3d0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_vector_product0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[6+1];
    
    char const* keywords[] = {"ax", "ay", "az", "bx", "by", "bz",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOOOOO",
                                     (char**)keywords , &args_obj[0], &args_obj[1], &args_obj[2], &args_obj[3], &args_obj[4], &args_obj[5]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]) && is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5]))
        return to_python(vector_product0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[1]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[2]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[3]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[4]), from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long,long>>>(args_obj[5])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft", "\n""    - __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft(float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin", "\n""    - __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft", "\n""    - __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft", "\n""    - __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__project_perpk3d(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d1(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__project_perpk3d", "\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop1(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop", "\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_loop_spectra_kzkh(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_loop_spectra_kzkh0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "loop_spectra_kzkh", "\n""    - loop_spectra_kzkh(float64[:,:,:], float64[:], float64[:,:,:], float64[:], float64[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_loop_spectra3d(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_loop_spectra3d0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "loop_spectra3d", "\n""    - loop_spectra3d(float64[:,:,:], float64[:], float64[:,:,:])", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_vector_product(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_vector_product0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "vector_product", "\n""    - vector_product(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "__for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft,
    METH_VARARGS | METH_KEYWORDS,
    "Compute the z component of the curl in spectral space.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft(float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:])"},{
    "__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin,
    METH_VARARGS | METH_KEYWORDS,
    "Return the curl of a vector in spectral space.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])"},{
    "__for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft,
    METH_VARARGS | METH_KEYWORDS,
    "Return the curl of a vector in spectral space.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])"},{
    "__for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft,
    METH_VARARGS | METH_KEYWORDS,
    "Return the divergence of a vector in spectral space.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__divfft_from_vecfft(float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])"},{
    "__for_method__OperatorsPseudoSpectral3D__project_perpk3d",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__project_perpk3d,
    METH_VARARGS | METH_KEYWORDS,
    "Project (inplace) a vector perpendicular to the wavevector.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])\n""\n""        The resulting vector is divergence-free.\n""\n"""},{
    "__for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop",
    (PyCFunction)__pythran_wrapall___for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop,
    METH_VARARGS | METH_KEYWORDS,
    "Project (inplace) a vector perpendicular to the wavevector.\n""\n""    Supported prototypes:\n""\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])\n""    - __for_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], complex128[:,:,:], complex128[:,:,:], complex128[:,:,:])\n""\n""        The resulting vector is divergence-free.\n""\n"""},{
    "loop_spectra_kzkh",
    (PyCFunction)__pythran_wrapall_loop_spectra_kzkh,
    METH_VARARGS | METH_KEYWORDS,
    "Compute the kz-kh spectrum.\n""\n""    Supported prototypes:\n""\n""    - loop_spectra_kzkh(float64[:,:,:], float64[:], float64[:,:,:], float64[:], float64[:,:,:])"},{
    "loop_spectra3d",
    (PyCFunction)__pythran_wrapall_loop_spectra3d,
    METH_VARARGS | METH_KEYWORDS,
    "Compute the 3d spectrum.\n""\n""    Supported prototypes:\n""\n""    - loop_spectra3d(float64[:,:,:], float64[:], float64[:,:,:])"},{
    "vector_product",
    (PyCFunction)__pythran_wrapall_vector_product,
    METH_VARARGS | METH_KEYWORDS,
    "Compute the vector product.\n""\n""    Supported prototypes:\n""\n""    - vector_product(float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:], float64[:,:,:])\n""\n""    Warning: the arrays bx, by, bz are overwritten.\n""\n"""},
    {NULL, NULL, 0, NULL}
};


            #if PY_MAJOR_VERSION >= 3
              static struct PyModuleDef moduledef = {
                PyModuleDef_HEAD_INIT,
                "operators",            /* m_name */
                "",         /* m_doc */
                -1,                  /* m_size */
                Methods,             /* m_methods */
                NULL,                /* m_reload */
                NULL,                /* m_traverse */
                NULL,                /* m_clear */
                NULL,                /* m_free */
              };
            #define PYTHRAN_RETURN return theModule
            #define PYTHRAN_MODULE_INIT(s) PyInit_##s
            #else
            #define PYTHRAN_RETURN return
            #define PYTHRAN_MODULE_INIT(s) init##s
            #endif
            PyMODINIT_FUNC
            PYTHRAN_MODULE_INIT(operators)(void)
            #ifndef _WIN32
            __attribute__ ((visibility("default")))
            #if defined(GNUC) && !defined(__clang__)
            __attribute__ ((externally_visible))
            #endif
            #endif
            ;
            PyMODINIT_FUNC
            PYTHRAN_MODULE_INIT(operators)(void) {
                import_array()
                #if PY_MAJOR_VERSION >= 3
                PyObject* theModule = PyModule_Create(&moduledef);
                #else
                PyObject* theModule = Py_InitModule3("operators",
                                                     Methods,
                                                     ""
                );
                #endif
                if(! theModule)
                    PYTHRAN_RETURN;
                PyObject * theDoc = Py_BuildValue("(sss)",
                                                  "0.11.0",
                                                  "2022-02-04 12:35:07.907548",
                                                  "35f4c87e14069f65603856963b39fedd6ad8cb1f60e97153ea35feb3ba1ae0f7");
                if(! theDoc)
                    PYTHRAN_RETURN;
                PyModule_AddObject(theModule,
                                   "__pythran__",
                                   theDoc);

                PyModule_AddObject(theModule, "__transonic__", __transonic__);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft", __code_new_method__OperatorsPseudoSpectral3D__rotzfft_from_vxvyfft);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin", __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft_outin);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft", __code_new_method__OperatorsPseudoSpectral3D__rotfft_from_vecfft);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft", __code_new_method__OperatorsPseudoSpectral3D__divfft_from_vecfft);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__project_perpk3d", __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d);
PyModule_AddObject(theModule, "__code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop", __code_new_method__OperatorsPseudoSpectral3D__project_perpk3d_noloop);
                PYTHRAN_RETURN;
            }

#endif