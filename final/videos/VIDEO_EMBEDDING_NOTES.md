# Video Embedding Notes

GitHub README pages do not reliably render repo-local HTML video tags. The root
README therefore uses a poster image with links, and the GitHub Pages demo page
provides the reliable pauseable video player.

GitHub issue and pull request comment boxes can accept uploaded `.mp4`, `.mov`,
and `.webm` files. After upload, GitHub creates an anonymized media URL that can
sometimes be placed directly in a README for inline playback. H.264 MP4 is the
recommended format for broad browser compatibility.

If an inline README video is still desired, upload
`final/videos/previews/best_ppo_demo_preview.mp4` to a GitHub issue or comment
box, copy the generated URL, and place that URL alone under the README demo
section. Only replace the poster block after the rendered README has been
visually verified.

Do not use a placeholder URL in the README.
