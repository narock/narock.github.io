---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Peer reviewed publications are available on my <a href="https://scholar.google.com/citations?user=ZnoM_joAAAAJ&hl=en"> Google Scholar profile</a>.

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
