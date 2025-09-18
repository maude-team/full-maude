# Full Maude

This repo contains the latest version of Full Maude. If you are looking for the Maude system or information on it, please go to the [Maude official site](http://maude.cs.uiuc.edu/).

The current version of Full Maude is [FM 3.5.1](sr/fm3/full-maude351.maude).

During the development of the Maude system we have put special emphasis on the creation of metaprogramming facilities to allow the generation of execution environments for a wide variety of languages and logics. The first most obvious area where Maude can be used as a metalanguage is in building language extensions for Maude itself. Our experience in this regard is very encouraging.

Full Maude is an extension of Maude written in Maude itself. Full Maude adds notation for object-oriented programming, parameterized views, module expressions specifying tuples of any size, etc. Although the Maude distribution has included the specification/implementation of Full Maude since it was first distributed in 1999, Core Maude and Full Maude are now closer than ever before. Many of the features now available in Core Maude, like parameterized modules, views, and module expressions like summation, renaming and instantiation, were available in Full Maude long before they were available in Core Maude. In fact, Full Maude has not only been a complement to Core Maude, but also a vehicle to experiment with new language features. Once these features have been mature enough to be implemented in the core language, we have made the effort to do so. Similarly, it is very likely that those features in Full Maude which are not yet available in Core Maude will become part of it sooner or later, and that new features will be added to Full Maude for purposes of language design and experimentation.

Full Maude implements a complete user interface for the extended language. Using the META-LEVEL and LOOP-MODE modules, we have been able to define in Core Maude all the additional functionality required for parsing, evaluating, and pretty-printing modules in the extended language, and also for input/output interaction. Thanks to the efficient implementation of the Maude rewrite engine, the parser, and the META-LEVEL module, such a language extension executes with reasonable efficiency.

For details on how to use the Maude system, and Full Maude, see the [Maude manual](https://maude.lcc.uma.es/maude-manual/maude-manual.html).

