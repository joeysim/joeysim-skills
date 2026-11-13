---
name: i-lost-the-plot
description: Use when the user types /i-lost-the-plot, or asks for the i-lost-the-plot skill by name.
metadata:
  version: "1.1.0"
  internal: true
---

# I Lost the Plot (renamed)

This skill is now named `www`, for "where were we". Its instructions did not change.

1. If the `www` skill is available, load it now and follow it. Use the user's message as the request.
2. If the `www` skill is not available, tell the user to install it:

   ```sh
   npx skills add joeysim/joeysim-skills --skill www
   ```

   Then the user can say "where were we", "I lost the plot", or type `/www`.
