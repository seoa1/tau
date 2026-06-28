---
title: Why "Tau"?
description: A friendly, non-mathy explanation of the circle constant τ — and why so many beautiful equations look even better with it.
hide:
  - navigation
  - toc
  - edit
---

<div class="tau-landing">
<div class="wrap">
  <nav>
    <div class="brand">
      <span class="glyph">&#964;</span>
      <span class="name">tau</span>
      <span class="ver">v0.1</span>
    </div>
    <div class="navlinks">
      <a href="../">Home</a>
      <a href="../getting-started/">Docs</a>
      <a href="../01-architecture/">Architecture</a>
      <a class="gh" href="https://github.com/alejandro-ao/tau">GitHub &#8599;</a>
    </div>
  </nav>

  <header>
    <div class="hero-grid">
      <div>
        <p class="eyebrow">The circle constant</p>
        <h1>Why we named it <em>&#964;</em>.</h1>
        <p class="lede">
          <strong>&#964; (tau)</strong> is a number many mathematicians wish we'd
          been teaching all along. You don't need to be a "math person" to get it
          &mdash; making it easy to get is the entire reason &#964; exists.
        </p>
        <p class="lede small-lede">
          <strong>&#964; = 2&#960; &#8776; 6.283.</strong> It's the circle constant
          measured from the <em>radius</em> instead of the diameter &mdash; and that
          one small change makes the math line up with how you already think.
        </p>
      </div>

      <figure class="figure">
        <span class="figlabel">&#952; sweeps 0 &rarr; &#964;</span>
        <canvas id="tauCanvas" width="520" height="380" role="img"
          aria-label="A radius sweeping a unit circle through one full turn, tracing one period of a sine wave."></canvas>
        <span class="figval" id="thetaVal">&#952; = 0.00</span>
      </figure>
    </div>

    <div class="strip arch-strip">
      <div class="cellitem"><span class="num">radius</span><span class="cap">the honest center</span></div>
      <div class="cellitem"><span class="num">one turn</span><span class="cap">equals &#964;</span></div>
      <div class="cellitem"><span class="num">cleaner</span><span class="cap">equations &amp; identities</span></div>
    </div>
  </header>
</div>

<div class="wrap">

  <section>
    <div class="two">
      <div>
        <p class="eyebrow">Start here</p>
        <h2>What even <em>is</em> &#964;?</h2>
        <p>Take a circle and grab its <strong>radius</strong> &mdash; the distance from the center to the edge. Now lay that radius along the rim, end to end, and count how many times it fits.</p>
        <p>The answer is always the same: about <strong>6.28</strong> radii, no matter how big or small the circle. That number is &#964;. It's just <em>"how many radii go around a circle."</em></p>
        <p class="small-lede">Watch the circle below unroll. Its edge stretches out to exactly &#964; radii long &mdash; one full turn.</p>
      </div>
      <figure class="figure wide">
        <span class="figlabel">one turn unrolled = &#964; &middot; r</span>
        <canvas id="rollCanvas" width="520" height="240" role="img"
          aria-label="A circle rolling along a line for one full turn, leaving a track exactly tau times its radius long."></canvas>
      </figure>
    </div>
  </section>

  <section>
    <div class="two boundary-two">
      <div>
        <p class="eyebrow">The problem with &#960;</p>
        <h2>We measured from the wrong place.</h2>
        <p>A circle is defined by its <strong>radius</strong> &mdash; every point the same distance from a center. Nobody draws a circle by picking a diameter first.</p>
        <p>But &#960; is built on the <em>diameter</em> (&#960; = circumference &divide; diameter). So our most famous constant starts from a measurement that isn't really fundamental. That tiny mismatch doesn't break anything &mdash; it just quietly makes formulas a little more awkward than they need to be, forever.</p>
        <p>Switch to the radius and you get &#964;. Suddenly things that used to need a stray factor of 2 just&hellip; don't.</p>
      </div>
      <div class="terminal" aria-hidden="true">
        <div class="bar"><span></span><span></span><span></span><span class="t">circle &mdash; definition</span></div>
<pre><span class="out">a circle =</span> <span class="key">all points at distance r</span>
<span class="out">          </span> <span class="key">from a center</span>

<span class="cmd">&#960;</span> = circumference / <span class="out">diameter</span>   <span class="out"># built on the leftover</span>
<span class="cmd">&#964;</span> = circumference / <span class="key">radius</span>     <span class="out"># built on the real thing</span>

<span class="out">so</span> <span class="key">&#964; = 2&#960;</span></pre>
      </div>
    </div>
  </section>

  <section>
    <div class="sec-head">
      <span class="mark">01</span>
      <h2>Angles finally make sense</h2>
    </div>
    <div class="two">
      <div>
        <p>Here's where &#964; earns its keep. Think about turning all the way around once &mdash; a full spin.</p>
        <p>With &#964;, <strong>one full turn is just &#964;</strong>. So any slice of a turn reads straight off the fraction: half a turn is &#964;/2, a quarter turn is &#964;/4, a twelfth is &#964;/12. The bottom number literally tells you the fraction of the circle.</p>
        <p>With &#960; you have to mentally double everything first &mdash; a quarter turn is &#960;/2? &mdash; and that little stumble is exactly where a lot of people first decide they're "bad at math."</p>
        <p class="small-lede">Watch the wedge sweep around. The readout shows the fraction of a full turn directly.</p>
      </div>
      <figure class="figure">
        <span class="figlabel">fraction of a turn</span>
        <canvas id="angleCanvas" width="440" height="400" role="img"
          aria-label="A wedge sweeping around a circle, with quarter-turn markers labelled in tau, and a readout of the fraction of a full turn."></canvas>
      </figure>
    </div>

    <div class="turns">
      <div class="turn-row turn-head">
        <span>fraction of a turn</span><span class="pi">with &#960;</span><span class="ta">with &#964;</span>
      </div>
      <div class="turn-row"><span>full turn</span><span class="pi">\(2\pi\)</span><span class="ta">\(\tau\)</span></div>
      <div class="turn-row"><span>half turn</span><span class="pi">\(\pi\)</span><span class="ta">\(\tau/2\)</span></div>
      <div class="turn-row"><span>quarter turn</span><span class="pi">\(\pi/2\)</span><span class="ta">\(\tau/4\)</span></div>
      <div class="turn-row"><span>an eighth</span><span class="pi">\(\pi/4\)</span><span class="ta">\(\tau/8\)</span></div>
      <div class="turn-row"><span>a twelfth</span><span class="pi">\(\pi/6\)</span><span class="ta">\(\tau/12\)</span></div>
    </div>
  </section>

  <section>
    <div class="sec-head">
      <span class="mark">02</span>
      <h2>The famous equations get prettier too</h2>
    </div>
    <p class="turns-note" style="margin-bottom:40px;">&#964; isn't just training wheels for beginners &mdash; it actually makes the grown-up results cleaner. Here are a few favorites, side by side.</p>

    <div class="two" style="margin-bottom:48px;">
      <div>
        <p class="eyebrow">Euler's identity</p>
        <h2>"The most beautiful equation."</h2>
        <p>The &#960; version, \(e^{i\pi} + 1 = 0\), is a famous brain-teaser &mdash; gorgeous, but you have to decode it.</p>
        <p>The &#964; version just <em>says what it means</em>: spin a point all the way around the circle (an angle of &#964;) and you land exactly back where you started, at 1.</p>
        <div class="eq-cols" style="margin-top:18px;">
          <div class="eq-col"><span class="lbl">with &#960;</span><span class="form">\(e^{i\pi} + 1 = 0\)</span></div>
          <div class="eq-col tau-col"><span class="lbl">with &#964;</span><span class="form">\(e^{i\tau} = 1\)</span></div>
        </div>
      </div>
      <figure class="figure">
        <span class="figlabel">a full turn lands on 1</span>
        <canvas id="eulerCanvas" width="420" height="380" role="img"
          aria-label="A unit vector rotating around the complex plane; after a full turn of tau it returns to the point 1."></canvas>
      </figure>
    </div>

    <div class="eq-list">
      <div class="eq">
        <span class="eq-title">Area of a circle</span>
        <div class="eq-cols">
          <div class="eq-col"><span class="lbl">with &#960;</span><span class="form">\(A = \pi r^2\)</span></div>
          <div class="eq-col tau-col"><span class="lbl">with &#964;</span><span class="form">\(A = \tfrac{1}{2}\,\tau r^2\)</span></div>
        </div>
        <p class="eq-note">The &#960; form looks shorter, but it hides a pattern. The &#964; form reveals that a circle's area belongs to the same family as half the formulas in physics class &mdash; the "one-half times a constant times something squared" shape:</p>
        <div class="family">
          <div><span class="form">\(\tfrac{1}{2} g t^2\)</span><small>distance fallen</small></div>
          <div><span class="form">\(\tfrac{1}{2} k x^2\)</span><small>spring energy</small></div>
          <div><span class="form">\(\tfrac{1}{2} m v^2\)</span><small>kinetic energy</small></div>
          <div class="fam-tau"><span class="form">\(\tfrac{1}{2} \tau r^2\)</span><small>circle area</small></div>
        </div>
      </div>

      <div class="eq">
        <span class="eq-title">The bell curve &mdash; the shape behind almost all of statistics</span>
        <div class="eq-cols">
          <div class="eq-col"><span class="lbl">with &#960;</span><span class="form">\(\dfrac{1}{\sqrt{2\pi}\,\sigma}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}\)</span></div>
          <div class="eq-col tau-col"><span class="lbl">with &#964;</span><span class="form">\(\dfrac{1}{\sqrt{\tau}\,\sigma}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}\)</span></div>
        </div>
        <p class="eq-note">That awkward \(\sqrt{2\pi}\) on the front? It collapses into a single tidy \(\sqrt{\tau}\).</p>
      </div>

      <div class="eq">
        <span class="eq-title">The Fourier transform &mdash; the math inside audio, images, JPEG, and your voice on a call</span>
        <div class="eq-cols">
          <div class="eq-col"><span class="lbl">with &#960;</span><span class="form">\(F(k)=\int f(x)\,e^{-2\pi i k x}\,dx\)</span></div>
          <div class="eq-col tau-col"><span class="lbl">with &#964;</span><span class="form">\(F(k)=\int f(x)\,e^{-i\tau k x}\,dx\)</span></div>
        </div>
        <p class="eq-note">The \(2\pi\) that tags along in nearly every wave and signal equation was always just one thing: &#964;.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="two boundary-two">
      <div>
        <p class="eyebrow">So why name the project &#964;?</p>
        <h2>Find the right radius.</h2>
        <p>A lot of "how AI agents work" material is like &#960; &mdash; technically correct, but built around the wrong center, so simple ideas end up looking complicated and people bounce off.</p>
        <p>Tau, the project, tries to do what &#964; the number does: find the small, honest core, then build outward from there so the rest becomes obvious. Pick the definition that makes everything else make sense.</p>
      </div>
      <div class="terminal" aria-hidden="true">
        <div class="bar"><span></span><span></span><span></span><span class="t">tau &mdash; the idea</span></div>
<pre><span class="pmt">&#964; &rsaquo;</span> <span class="cmd">explain agents simply</span>

<span class="out">  find    </span><span class="key">the small honest core</span>
<span class="out">  build   </span><span class="key">outward from there</span>
<span class="out">  result  </span><span class="key">the rest looks obvious</span></pre>
      </div>
    </div>
  </section>

  <section class="closing">
    <span class="turn">&#964;</span>
    <p>Same instinct, applied to code: pick the center that makes everything line up &mdash; then go see how Tau is built.</p>
    <div class="cta-row">
      <a class="ghost" href="../getting-started/">Get started <span class="arr">&rarr;</span></a>
      <a class="ghost" href="../01-architecture/">See the architecture <span class="arr">&rarr;</span></a>
      <a class="ghost" href="https://www.tauday.com/tau-manifesto">Read the full Tau Manifesto <span class="arr">&rarr;</span></a>
    </div>
  </section>

  <footer>
    <div class="brand">
      <span class="glyph" style="font-size:20px;">&#964;</span>
      <span class="name">tau</span>
    </div>
    <div class="l">
      <a href="../">Home</a>
      <a href="../getting-started/">Docs</a>
      <a href="https://github.com/alejandro-ao/tau">GitHub</a>
      <a href="https://www.tauday.com/tau-manifesto">Tau Manifesto</a>
    </div>
    <span>An educational project &middot; inspired by Pi</span>
  </footer>
</div>
</div>
