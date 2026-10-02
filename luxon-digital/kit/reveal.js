(function () {
  var els = document.querySelectorAll('.lxk .rv:not(.in)');
  if (!('IntersectionObserver' in window)) { for (var i = 0; i < els.length; i++) els[i].classList.add('in'); return; }
  var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .1 });
  for (var j = 0; j < els.length; j++) io.observe(els[j]);
})();
