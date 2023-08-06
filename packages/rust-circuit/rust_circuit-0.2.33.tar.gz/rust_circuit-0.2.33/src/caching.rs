/// Generates a caching struct which can use any of the caches from the
/// `cached` crate.
///
/// Uses [caching_method](crate::caching_method) to generate the methods, so
/// see the documentation for that macro for the method declaration syntax.
///
/// # Example
/// ```
/// # use rust_circuit::caching_struct;
/// # use cached::Cached;
/// caching_struct!(
///     pub struct Function;
///     [pub my_cache_name : T] pub fn c(&mut self_, a : u64) -> u64 = {
///         match a {
///             0 => 0,
///             1 => 1,
///             n => self_.c(n - 1) + self_.c(n - 2),
///         }
///     }
/// );
///
/// let mut func = Function::unbounded();
///
/// assert_eq!(func.c(0), 0);
/// assert_eq!(func.c(1), 1);
/// assert_eq!(func.c(7), 13);
/// assert_eq!(func.c(85), 259695496911122585);
///
/// assert_eq!(func.my_cache_name.cache_size(), 86);
/// ```
///
/// Because I'm a mad lad, this macro supports much more insane syntax.
/// ```
/// # use rust_circuit::caching_struct;
/// # use cached::Cached;
/// caching_struct!(
///     #[derive(Debug)] // (this derive does nothing in example because F/J/V don't impl)
///
///     // lifetimes + isolated type identifiers have to go up front in braces
///     // each bound identifier must be in braces
///     // (this is because rust doesn't support nice macro parsing of trait bounds)
///     pub struct CrazyStruct<{'a, 'b, V}, {F: Fn(u8) -> u16}, {J : Clone + std::fmt::Debug}>
///     where { // you can do where bound, but must be in braces also
///         i8 : Into<J>,
///         V : Into<J> + Clone,
///         J : PartialEq,
///     }
///     {
///         a : &'a F,
///         b : &'b J,
///         _mark : std::marker::PhantomData<V>,
///     }
///     
///     [pub first_cache : T] pub fn first_cached(&mut self_, a : u64) -> J = {
///         if a < 7 {
///             self_.b.clone()
///         } else {
///             let x : i8 = 12;
///             x.into()
///         }
///     }; // if you want to declare multiple functions, you need to delimit with ';'
///
///     // You can prepend a list of arguments in braces which won't be cached.
///     // They should remain fixed if you want the cache to be correct!
///     [pub snd_cache : L] pub fn snd_cached(&mut self_, {should_be_fixed_per_cache : &V}, b : u8) -> u16 = {
///         let as_j : J = should_be_fixed_per_cache.clone().into();
///         if as_j == 4i8.into() {
///             (self_.a)(b)
///         } else {
///             7
///         }
///     };
///
///     // You can also specify a key.
///     [pub third_cache : N]
///     {Key : u8 = hash_me_mod_3 % 3}
///     pub fn third_cached(&mut self_, not_used_for_cache_also : &V, hash_me_mod_3 : u8) -> u16 = {
///         let as_j : J = not_used_for_cache_also.clone().into();
///         if as_j == 4i8.into() {
///             (self_.a)(hash_me_mod_3)
///         } else {
///             7
///         }
///     };
/// );
///
/// let func = |x : u8| x as u16;
/// let mut crazy = CrazyStruct::unbounded(&func, &8, std::marker::PhantomData::<i8>::default());
///
/// let _ = crazy.first_cached(8);
/// let _ = crazy.first_cached(11);
///
/// assert_eq!(crazy.snd_cached(&4, 11), 11);
/// assert_eq!(crazy.snd_cached(&8, 11), 11); // wrong because reference is different from previous!
/// assert_eq!(crazy.snd_cached(&8, 10), 7);
/// assert_eq!(crazy.snd_cached(&8, 3), 7);
///
/// assert_eq!(crazy.third_cached(&4, 11), 11);
/// assert_eq!(crazy.third_cached(&8, 11), 11); // wrong because reference is different from previous!
/// assert_eq!(crazy.third_cached(&8, 10), 7);
/// assert_eq!(crazy.third_cached(&8, 3), 7);
/// assert_eq!(crazy.third_cached(&8, 6), 7); // wrong because hashes mod 3
///
/// assert_eq!(crazy.first_cache.cache_size(), 2);
/// assert_eq!(crazy.snd_cache.cache_size(), 3);
/// assert_eq!(crazy.third_cache.cache_size(), 3);
/// ```
#[macro_export]
macro_rules! caching_struct {
    // now *this* is peak rust dev
    // TODO: macro is kinda messy, maybe I should clean this up somehow???
     // TODO: use https://veykril.github.io/tlborm/decl-macros/building-blocks/parsing.html
    (
    $(#[$top_attr:meta])*
    $struct_vis:vis struct $structname:ident
    $(<
        $({$($struct_lifetime:lifetime),* $(,)? $($isolated_struct_typing_ident:ident),* $(,)?} $(,)?)?
        $({$struct_typing_ident:ident : $($struct_type_item:tt)*}),+
    >)?
    $(where {$($where_items:tt)*})?
    $({
        $($field_vis:vis $field_name:ident : $field_type:ty),* $(,)?
    })? $(;)?
    $(
        [$cache_vis:vis $cache_name:ident : $cache_type:ident]
        $([$cached_to_func_vis:vis $(,)? $($cached_to_func_name:ident)?])?
        $({$($key_stuff : tt)*})?
        $func_vis:vis fn $fn_name:ident (&mut $self_id:ident,
            $({$($arg_no_cache:ident : $argtype_no_cache:ty),+ $(,)?},)?
            $($arg:ident : $argtype:ty),+ $(,)?)
        -> $ret:ty = $body:expr
    );+ $(;)?
    ) => {
        $(#[$top_attr])*
        $struct_vis struct $structname<
            $($($($struct_lifetime,)* $($isolated_struct_typing_ident,)*)*
                $($struct_typing_ident : $($struct_type_item)*,)*)*
            $(
                $cache_type : cached::Cached<$crate::make_key_type_impl!($({$($key_stuff)*})* {$($argtype,)*}), $ret>,
            )*>
        $(where $($where_items)*)*
        {
            $(
                $cache_vis $cache_name : $cache_type,
            )*
            $($(
                $field_vis $field_name : $field_type,
            )*)*
        }

        // TODO: more niceness functions?
        impl< $($($($struct_lifetime,)* $($isolated_struct_typing_ident,)*)*
            $($struct_typing_ident : $($struct_type_item)*,)*)*>
            $structname<
                $($($($struct_lifetime,)* $($isolated_struct_typing_ident,)*)*
                $($struct_typing_ident,)*)*
            $(
            cached::UnboundCache<$crate::make_key_type_impl!($({$($key_stuff)*})* {$($argtype,)*}), $ret>,
        )*>
        $(where $($where_items)*)*
        {
            pub fn unbounded($($($field_name : $field_type,)*)*) -> Self {
                Self {
                    $(
                        $cache_name : cached::UnboundCache::new(),
                    )*
                    $($($field_name,)*)*
                }
            }
        }

        impl<
            $($($($struct_lifetime,)* $($isolated_struct_typing_ident,)*)*
            $($struct_typing_ident : $($struct_type_item)*,)*)*
            $(
                $cache_type : cached::Cached<$crate::make_key_type_impl!($({$($key_stuff)*})* {$($argtype,)*}), $ret>
            ),*
        > $structname<$($($($struct_lifetime,)* $($isolated_struct_typing_ident,)*)*
                        $($struct_typing_ident,)*)* $($cache_type,)*>
        $(where $($where_items)*)*
        {
            $(
                $crate::caching_method!(
                    [$cache_name] $([$cached_to_func_vis, $($cached_to_func_name)*])*
                    $({$($key_stuff)*})*
                    $func_vis fn $fn_name (&mut $self_id,
                        $({$($arg_no_cache : $argtype_no_cache,)*}, )*
                        $($arg : $argtype),+) -> $ret = $body
                );
            )*
        }

    };
}

#[doc(hidden)]
#[macro_export]
macro_rules! make_key_expr_impl {
    ({Key : $key_type:ty = $key_expr:expr} {$($args_tt:tt)*}) => (
        $key_expr
    );

    ({$($arg:expr),* $(,)?}) => (
        ($($arg,)*)
    );
}

#[doc(hidden)]
#[macro_export]
macro_rules! make_key_type_impl {
    ({Key : $key_type:ty = $key_expr:expr} {$($args_tt:tt)*}) => (
        $key_type
    );

    ({$($key_type:ty),* $(,)?}) => (
        ($($key_type,)*)
    );
}

#[doc(hidden)]
#[macro_export]
macro_rules! repeated_tuple_impl {
    ([$({$($running:tt)*})*] {$($stuff:tt)*} ($first:ident $(,)? $($items:ident),* $(,)?)) => (
        $crate::repeated_tuple_impl!([$({$($running)*})* {$($stuff)*}] {$($stuff)*} ($($items),*))
    );

    ({$($stuff:tt)*} ($($items:ident),* $(,)?)) => (
        $crate::repeated_tuple_impl!([] {$($stuff)*} ($($items),*))
    );

    ([$({$($running:tt)*})*] {$($stuff:tt)*} ()) => (
        ($($($running)*,)*)
    );
}

/// Sets up caching for a given method.
/// (used by [caching_struct](crate::caching_struct) macro, so those examples also applicable)
///
/// # Example
/// ```
/// # use rust_circuit::caching_method;
/// # use cached::Cached;
/// struct FunctionWithCache {
///     my_cache_name: cached::UnboundCache<(u64,), u64>,
/// }
///
/// impl FunctionWithCache {
///     caching_method!(
///         [my_cache_name] pub fn c(&mut self_, a : u64) -> u64 = {
///             match a {
///                 0 => 0,
///                 1 => 1,
///                 n => self_.c(n - 1) + self_.c(n - 2),
///             }
///         }
///     );
/// }
///
/// let mut func = FunctionWithCache{ my_cache_name : cached::UnboundCache::new() };
///
/// assert_eq!(func.c(0), 0);
/// assert_eq!(func.c(1), 1);
/// assert_eq!(func.c(7), 13);
/// assert_eq!(func.c(85), 259695496911122585);
///
/// assert_eq!(func.my_cache_name.cache_size(), 86);
/// ```
///
/// The macro allow supports generating a method to create a bound version of the function.
///
/// ```
/// # use rust_circuit::caching_method;
/// # use cached::Cached;
/// struct FunctionWithCache {
///     my_cache_name: cached::UnboundCache<(u64,), u64>,
/// }
///
/// impl FunctionWithCache {
///     caching_method!(
///         // defaults to generating $fn_name + _bound if you add brackets like this
///         // (',' required if empty for default)
///         [my_cache_name] [,] pub fn c(&mut self_, a : u64) -> u64 = {
///             match a {
///                 0 => 0,
///                 1 => 1,
///                 n => self_.c(n - 1) + self_.c(n - 2),
///             }
///         }
///     );
/// }
/// let mut func = FunctionWithCache {
///     my_cache_name: cached::UnboundCache::new(),
/// };
///
/// let mut bound = func.c_bound();
/// assert_eq!(bound(0), 0);
/// assert_eq!(bound(1), 1);
/// assert_eq!(bound(7), 13);
/// assert_eq!(bound(85), 259695496911122585);
/// drop(bound);
///
/// assert_eq!(func.my_cache_name.cache_size(), 86);
///
/// // you can also specify a name or just visibility like this
/// impl FunctionWithCache {
///     caching_method!(
///         // these could use a different cache or the same one, either works
///         [my_cache_name] [pub bind_other_func_with_some_name] pub fn other_func(&mut self_, a : u64) -> u64 = {
///             self_.c(a)
///         }
///     );
///
///     caching_method!(
///         // you can also just provide visability
///         [my_cache_name] [pub,] pub fn and_one_last_func(&mut self_, a : u64) -> u64 = {
///             self_.c(a)
///         }
///     );
/// }
///
/// let mut func = FunctionWithCache {
///     my_cache_name: cached::UnboundCache::new(),
/// };
///
/// let mut bound = func.bind_other_func_with_some_name();
/// assert_eq!(bound(85), 259695496911122585);
/// drop(bound);
///
/// let mut bound = func.and_one_last_func_bound();
/// assert_eq!(bound(85), 259695496911122585);
/// drop(bound);
/// ```
///
/// It's also possible to have uncached arguments via prepending these arguments in {...}.
/// ```
/// # use rust_circuit::caching_method;
/// # use cached::Cached;
/// struct FunctionWithCache {
///     my_cache_name: cached::UnboundCache<(u64,), u64>,
/// }
///
/// impl FunctionWithCache {
///     caching_method!(
///         [my_cache_name] [,] pub fn pass_ref_func(&mut self_, {b : &u64}, a : u64) -> u64 = {
///             a + b
///         }
///     );
/// }
///
/// let mut func = FunctionWithCache {
///     my_cache_name: cached::UnboundCache::new(),
/// };
///
/// assert_eq!(func.pass_ref_func(&7, 8), 7 + 8);
/// // NOTE: this will be invalid if you change the reference!
/// assert_eq!(func.pass_ref_func(&6, 8), 7 + 8); // maybe not what you thought!
///
/// let mut bound = func.pass_ref_func_bound();
/// assert_eq!(bound(&3, 8), 7 + 8); // still hits same cache
/// assert_eq!(bound(&4, 4), 4 + 4);
/// ```
#[macro_export]
macro_rules! caching_method {
    ([$access_cache:tt]
     // TODO: use https://veykril.github.io/tlborm/decl-macros/building-blocks/parsing.html
     $({$($key_stuff:tt)*})?
     $func_vis:vis fn $fn_name:ident (&mut $self_id:ident,
         $({$($arg_no_cache:ident : $argtype_no_cache:ty),+ $(,)?},)?
         $($arg:ident : $argtype:ty),+ $(,)?) -> $ret:ty = $body:expr) => {
        $func_vis fn $fn_name(&mut self, $($($arg_no_cache : $argtype_no_cache,)*)* $($arg : $argtype,)* ) -> $ret {
            let key_val = $crate::make_key_expr_impl!($({$($key_stuff)*})* {$($arg.clone(),)*});

            if let Some(out) = self.$access_cache.cache_get(&key_val) {
                return out.clone();
            }

            let $self_id = self;
            let out = $body;
            $self_id.$access_cache.cache_set(key_val, out.clone());
            out

        }
    };

    ([$access_cache:tt] [$cached_to_func_vis:vis $cached_to_func_name:ident]
    $({$($key_stuff:tt)*})?
     $func_vis:vis fn $fn_name:ident (&mut $self_id:ident,
         $({$($arg_no_cache:ident : $argtype_no_cache:ty),+ $(,)?},)?
         $($arg:ident : $argtype:ty),+ $(,)?) -> $ret:ty = $body:expr) => {
        caching_method!([$access_cache] $({$($key_stuff)*})*
            $func_vis fn $fn_name  (&mut $self_id,
                $({$($arg_no_cache : $argtype_no_cache,)*},)*
                $($arg : $argtype),+) -> $ret = $body);

        $cached_to_func_vis fn $cached_to_func_name(&mut self) -> Box<dyn FnMut($($($argtype_no_cache,)*)* $($argtype,)*) -> $ret + '_> {
            Box::new(|$($($arg_no_cache : $argtype_no_cache,)*)* $($arg : $argtype,)*| self.$fn_name($($($arg_no_cache,)*)* $($arg,)*))
        }
    };

    ([$access_cache:tt] [$cached_to_func_vis:vis $(,)?]  $func_vis:vis fn $fn_name:ident $($other:tt)*) => {
        paste::paste! {
            caching_method!([$access_cache] [$cached_to_func_vis [<$fn_name _bound>]] $func_vis fn $fn_name $($other)*);
        }
    };
}

/// Generates a (possibly recursive) cached lambda.
///
/// Internally uses [caching_struct](crate::caching_struct).
///
/// Note that the lambda *must* be immutable, but it can capture.
///
/// # Example
///
/// ```
/// # use rust_circuit::cached_lambda;
/// let zero_start = 0;
/// let one_start = 1;
///
/// cached_lambda!{
///     let mut func = |a: u64| -> u64 = {
///         match a {
///             0 => zero_start,
///             1 => one_start,
///             n => func(n - 1) + func(n - 2),
///         }
///     };
/// };
///
/// assert_eq!(func(85), 259695496911122585);
/// assert_eq!(func(10), 55);
/// ```
///
/// You can also use a custom key expression.
///
/// ```
/// # use rust_circuit::cached_lambda;
/// let zero_start = 0;
/// let one_start = 1;
///
/// cached_lambda!{
///     {Key : u8 = (a % 20) as u8}
///     let mut mod_20_func = |a: u64| -> u64 = {
///         match a {
///             0 => zero_start,
///             1 => one_start,
///             n => mod_20_func(n - 1) + mod_20_func(n - 2),
///         }
///     };
/// };
///
/// assert_eq!(mod_20_func(10), 55);
/// assert_eq!(mod_20_func(30), 55);
/// assert_eq!(mod_20_func(30010), 55);
/// ```
///
/// Atm, this doesn't support caches other than unbounded, but would be easy to
/// implement. Also doesn't currently support accessing cache, but would also
/// be easy to add.
#[macro_export]
macro_rules! cached_lambda {
    {
        $({$($key_stuff : tt)*})?
        let mut $func_id:ident = |$($arg:ident : $argtype:ty),* $(,)?| -> $ret:ty  = $body:expr;
    } => {
        paste::paste! {
            // Use lambda in holder pattern to allow for recursion.
            // Then, pass holder immutably so borrow checking can see that it's fine.

            // We can't avoid boxing because lambdas can't refer to themselves.
            // Hopefully inlined out?
            type [<$func_id:camel KeyType>] = $crate::make_key_type_impl!($({$($key_stuff)*})* {$($argtype,)*});
            struct [<$func_id:camel OtherFuncHolder>]<'a, T: cached::Cached<[<$func_id:camel KeyType>], $ret>>(
                Box<dyn Fn(&mut [<$func_id:camel FuncHolder>]<T>, &Self, $($argtype,)*) -> $ret + 'a>,
            );

            $crate::caching_struct!(
                struct [<$func_id:camel FuncHolder>];
                [cache : T] $({$($key_stuff)*})*
                fn call(&mut self_, {func_arg : &[<$func_id:camel OtherFuncHolder>]<T>}, $($arg : $argtype,)*) -> $ret = {
                    func_arg.0(self_, func_arg, $($arg,)*)
                }
            );

            let other_holder = [<$func_id:camel OtherFuncHolder>](Box::new(
                |call_in: &mut [<$func_id:camel FuncHolder>]<cached::UnboundCache<_, _>>,
                 func_in: &[<$func_id:camel OtherFuncHolder>]<_>,
                 $($arg,)*| {
                    let mut $func_id = |$($arg,)*| call_in.call(func_in, $($arg,)*);
                    $body
                },
            ));

            // TODO: support other caching as needed
            let mut holder = [<$func_id:camel FuncHolder>]::unbounded();

            let mut $func_id = |$($arg,)*| holder.call(&other_holder, $($arg,)*);
        }
    }
}

/// Cache a callable. Just a wrapper on top of [cached_lambda](crate::cached_lambda).
///
/// Recursive calls won't (naively) be cached, so if you want that, use [cached_lambda](crate::cached_lambda).
///
/// ```
/// # use rust_circuit::cached_callable;
/// fn my_function(a : u64) -> u64 {
///     a + 3
/// }
///
/// cached_callable!{
///     let mut func : (|a : u64| -> u64) = my_function;
/// };
///
/// assert_eq!(func(85), 88);
///
/// ```
#[macro_export]
macro_rules! cached_callable {
    {
        $({$($key_stuff : tt)*})?
        let mut $func_id:ident : (|$($arg:ident : $argtype:ty),* $(,)?| -> $ret:ty)  = $callable:expr;
    } => {
        $crate::cached_lambda!(
            $({$($key_stuff)*})*
            let mut $func_id = |$($arg : $argtype,)*| -> $ret = $callable($($arg,)*);
        );
    }
}
