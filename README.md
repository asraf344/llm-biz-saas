This repo is based on the guideline by `Ed Donner's`  repo https://github.com/ed-donner/production which is used at his [AI Engineering Production Track](https://www.udemy.com/course/generative-and-agentic-ai-in-production) course. 

## Getting Started

This repos is based on Ed Donner's repo except it has used `Gemini API` rather than `openAI API`

To use it at vercel is quite easy:

```bash
$ vercel env add GEMINI_API_KEY
# Then create project at vercel
$ vercel link
# Then for preview
$ vercel .

# and for producttion
$ vercel --prod
```