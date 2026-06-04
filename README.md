# The Kindness Flywheel

An open-source publication exploring the hypothesis that kindness — operationalized as genuine care at every level of an organization — is the most defensible business strategy when AI commoditizes capability.

Not kindness instead of operational excellence. Kindness AND operational excellence — with the claim that in a post-convergence world, kindness is what makes operational excellence defensible.

Not theory. Lived experience. What's working, what's hard, what we're learning.

## The Five Lenses

- **#Strategy** — Convergence, trust, competitive advantage, the business case for kindness.
- **#People** — Education, professional development, culture, and behavior.
- **#Technology** — Product design, implementation, security and compliance, agent development.
- **#Practice** — Real organizational stories. What happened when we tried this.
- **#Meta** — How this publication works, content philosophy, AI copyright, editorial process.

## Contribute

Fork the repo. Write your story. Open a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Local development

To preview the site locally you need [Docker](https://www.docker.com/) — no Ruby toolchain required:

```
docker compose up
```

This builds the site in a `ruby:3.1` container and serves it at <http://localhost:4000> with auto-regeneration on file changes. Gems install into `vendor/bundle`. Stop with `Ctrl-C`, or `docker compose down`.

## License

All content is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, quote it, build on it. Just credit the author.
