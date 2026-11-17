# Hermes keeps failing or does odd things with posting

**Why:** Some models are weak at calling tools. Posting needs several correct tool calls in a row (upload picture, then create post). Small or overloaded models skip steps or send broken data.

**Fix:**
```
hermes -p public model
```
Pick a stronger model (for example a Gemini Pro model with your own Gemini key). Then `/exit` and start a new `public chat`: an open chat keeps the old model.

**Watch out:** Free or overloaded OpenRouter models may fail too. If the error says rate limit or no credits, it's the provider, not your setup. Postiz keeps scheduled posts even when Hermes fails, so a bad model can't stop a post that is already scheduled.
