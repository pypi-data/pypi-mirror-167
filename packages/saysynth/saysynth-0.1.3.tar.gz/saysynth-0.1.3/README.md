----------------------------

Generate music with Apple's `say` command.

Sounds like this:

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1231627354&color=%23ffffff&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/abelsonlive" title="brian abelson" target="_blank" style="color: #cccccc; text-decoration: none;">brian abelson</a> · <a href="https://soundcloud.com/abelsonlive/saymidi-example" title="saymidi example" target="_blank" style="color: #cccccc; text-decoration: none;"><code>saysynth</code> example</a></div>

## About
<hr/>

<code>saysynth</code> is a a synthesizer built on top of Apple's built-in [Speech Synthesis](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/SpeechOverview/SpeechOverview.html#//apple_ref/doc/uid/TP40004365-CH3-SW6) framework, which was first introduced nearly 30 years ago, when Steve Jobs demoed "Fred":

<center><iframe width="100%"  src="https://www.youtube.com/embed/NnsDFSXBWoM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

At some point in Fred's development, Apple decided they needed to give developers the ability to control the pitch and speaking rate of his voice. These capabilities were provided via a [domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language) (DSL) Apple created to specify the duration and pitch contours of individual [phonemes](https://en.wikipedia.org/wiki/Phoneme). Eventually, this DSL was expanded to support "Alex" and "Victoria", two other built-in voices. The syntax for this DSL looks something like this:

```
AA {D 120; P 176.9:0 171.4:22 161.7:61}
```

Where `AA` is a [valid phoneme](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/Phonemes/Phonemes.html#//apple_ref/doc/uid/TP40004365-CH9-SW1), `D 120` is the duration of the phoneme in milliseconds, and ` P 176.9:0 171.4:22 161.7:61` represents the pitch contour for the phoneme in colon-separated pairs of frequnecy and percentage duration.

<code>saysynth</code> works by harnessing this DSL to create musical passages with the `say` command, mapping notes onto their associated frequencies (via my associated library [`midi-utils`](https://gitlab.com/gltd/midi-utils/)), generating phonemes with pitch contours (as described in [Apple's Speech Synthesis Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/FineTuning/FineTuning.html#//apple_ref/doc/uid/TP40004365-CH5-SW7)), and spawning many subprocesses to create polyphonic, mostly drone-oriented music. Rudimentary text-to-speech capabilities are provided by [`g2p-en`](https://pypi.org/project/g2p-en/), a library for extracting phonemes from words, though, as of now, a lot of trial and error is necessary to get this to sound decent.

## Installation
<hr/>

<code>saysynth</code> only works on Mac OS X machines with a working `say` instllation. By default, the path to the executable is set to `/usr/bin/say`. You can override
that path by setting the environment variable `SAYSYNTH_SAY_EXECUTABLE`.

To install via `pypi` run:

```shell
pip install saysynth
```

**NOTE**: <code>saysynth</code> is in active development, so the API is likely to change. I'll follow [semantic versioning standards](https://semver.org/).

## Usage
<hr/>

Below are basic details on saysynth's built-in functionality. For a detailed overview on how to make music with saysynth, refer to this [blog post](https://brian./abelson.live/todo) or view the full API documentation at [saysynth.globally.ltd](https://saysynth.globally.ltd).

### Command-Line Interface (`sy`)
<hr/>

<code>saysynth</code> is primarily designed to be used via it's comamnd-line interface (`sy` for short).

You can view all commands (and their corresponding docs) by runnings `sy --help`:

```shell
Usage: sy [OPTIONS] COMMAND [ARGS]...

  Generate music with the `say` command.

Options:
  --help  Show this message and exit.

Commands:
  arp      Generate an arpeggiated melody
  chord    Generate a polyphonic chord.
  demo     Play a built-in demo.
  font     Given a scale and other parameters, generate a soundfont of...
  midi     Generate a melody from a monophonic midi file.
  note     Generate an individual note.
  seq      Play a sequence of `chord`, `midi`, `note`, and/or `arp`...
  stop     Stop currently running <code>saysynth</code> processes by passing in the...
  version  Print the current version of <code>saysynth</code> to the console.
```

#### **sy arp**
<hr/>

`sy arp` accepts a chord root (eg: C3), chord name, and list of styles to generate a melodic, arpeggiated sequence of speech synthesis.

_example_:

```shell
sy arp E0 -cn 0,3,5,7,9,12,14  -bb 160 -bc 1/16 -nb 160 -sl 'random_shuffle,random_octaves' -p m -vl 127 -l 300 -vpn 5 -vps 5 -x --text '. EY SEE EY BEE .' -sb 160 -sc 1/32
```

You can see the full list of options for this command via `sy arp --help`.

#### **sy chord**
<hr/>

`sy chord` accepts a chord root (eg: C3) or midi note number (eg: 69), a chord name (eg: min6), and other paremeters to spawn multiple `say` commands that generate a polyphonic chord.

_example_:

```shell
sy chord C1 -c min6 -db 155 -dc 64 -sb 155 -sc 1/2 -at 0.3 -de 0.3 -su 0.9 -re 0.4 -rs phoneme -rp Fred:drone -vr 0.1 0.50 -x
```

You can see the full list of options for this command via `sy chord --help`.

#### **sy demo**
<hr/>

`sy demo` is a wrapper for `sy seq` and allows you to play built-in demo sequences. Live recordings of these demos are also for sale on [bandcamp](https://buy.globally.ltd).

_example_:

```shell
sy demo play fire
```

You can see the full list of options for this command via `sy demo --help`.

#### **sy font**
<hr/>

`sy font` enables the generation of ["soundfonts"](https://www.maniactools.com/soft/midi_converter/soundfonts.shtml) or directories of individual soundfiles, which can be used in a sampler or DAW to create custom instruments. All synthesis parameters from `sy note` can be modified in `sy font`.

_example_:

```shell
sy font --scale-start-at C2 --scale-end-at C5 --scale=octatonic_whole --key C -v Fred -od tmp/ -f aiff --phoneme=m -d 1000 -rv 40 120
```

You can see the full list of options for this command via `sy font --help`.

#### **sy midi**
<hr/>

`sy midi` accepts a midi file and generates pitched phonemes. The midi files must be fully monophonic. (In other words there must not be any overlapping notes. Eventually I'll figure out this issue, but for now there is a helpful error message which indicates the name of an overlapping note and the time at which it occurs. You can then use this information to edit your midi file in whatever DAW you use. There is also no support for multi-track midi files, though that will be less challenging to implement.) `sy midi` then maps the notes in the midi file onto pitched phonemes


_example_:

**NOTE**: you must clone this repository and run this example from the root directory.

```shell
sy midi examples/arp.mid --phoneme m | say -v Fred
```

You can see the full list of options for this command via `sy midi --help`.

#### **sy note**
<hr/>

`sy note` accepts a note name (eg: C3) or midi note number (eg: 69) and generates input to the `say` command which makes a monophonic note.

_example_:

```shell
sy note D#3 -rp Fred:drone | say -v Fred &
```

You can see the full list of options for this command via `sy note --help`.

#### **sy seq**
<hr/>

`sy seq` accepts a `yaml` filepath specifying multiple <code>saysynth</code> commands to be concurrently executed.

The `yaml` file might look something like this:

```yaml
name: my-sequence # the name of the sequence
globals: # configurations shared between all tracks
  duration_bpm: 80
tracks: # list of tracks / configurations
  chord1:
    type: chord
    options:
      root: E3
      chord: min6
      duration_count: 128
      segment_bpm: 80
  note1:
    type: note
    options:
      start_bpm: 80
      start_count: 2
      root: F#3
```

Where `globals` define options shared between all `tracks`, each of which have a `type` which corresponds to a <code>saysynth</code> command (`chord`, `midi`, `note`, and/or `arp`) and a set of `options`.

##### **sy seq <cmd>**

`sy seq` provides multiple subcommands to control the behavior of your sequence. These include:

- `play`: Play the sequence as-is, from beginning to end, respecting any `start_*` configurations.
- `start`: Launch all tracks in the sequence immediately, irregardless of any `start_*` configurations.
- `stop`: Stop one or more tracks currently playing from the sequence.
- `echo`: Print the sequence to the console.
- `render`: Render all tracks in the sequence as separate, monophonic audio-files.

Each of these subcommands accepts command line flags, as well. For instance, `--tracks` allows you to
`play`, `start`, `stop`, or `render` only certain tracks in the sequence. Similarly `--audio-devices` allows
you to filter tracks which are configured to play on certain audio outputs. `--config-overrides` provides the ability to override global and track-level configurations at runtime by passing in yaml-formatted configurations, eg: `-c '{"foo":"bar"}'`. These configurations can be specified at the track-level by nesting them under the track name, eg: `-c '{"track":{"foo":"bar"}}'`. Finally, `--output-dir` allows you to specify the directory to write audio files into as a part of the `render` command.

_examples_:

```shell
sy seq play examples/hello-world.yml
sleep 10
sy seq stop examples/hello-world.yml -t hello_world
```

You can also see an archive of my past <code>saysynth</code> [performances](https://gitlab.com/gltd/saysynth/-/tree/main/performances) for examples of sequences.

You can see the full list of options for this command via `sy seq --help`.

#### **sy stop**
<hr/>

`sy stop` allows you to stop any track (and its children) via a `pid`. You can also pass in `all` to stop all running tracks.

_example_:

```shell
sy note D#3 -rp Fred:drone  -x
sleep 1
echo "stopping note now!"
sy stop all
```

#### **sy version**
<hr/>

<code>sy version</code> accepts a chord root (eg: C3) or midi note number (eg: 69) and generates multiple `say` commands generating a polyphonic chord.

_example_:

```
sy chord C1 -c min6 -db 155 -dc 64 -sb 155 -sc 1/2 -at 0.3 -de 0.3 -su 0.9 -re 0.4 -rs phoneme -rp Fred:drone -vr 0.1 0.50 -x
```

You can see the full list of options for this command via `sy chord --help`.

### Python API
<hr/>

Full python API documentation can be found be here: [saysynth.globally.ltd](https://saysynth.globally.ltd).

## Development / Contributing
<hr/>

If you're interested in contributing to <code>saysynth</code> or would like to report [an issue](https://gitlab.com/gltd/saysynth/-/issues), all development is done on [gitlab](https://gitlab.com/gltd/saysynth).  You can also reach out to me via `hey [at] gltd [dot] email`. I maintain an up-to-date [todo list](#todo) of the issues I'm currently working on below.

To install via `git` for local development:

  * clone this repo:
    - `git clone https://gitlab.com/gltd/saysynth.git`
  * create a virtualenv:
    - `cd saysynth && python -m venv .venv`
  * activate it:
    - `source .venv/bin/activate`
  * install the lib:
    - `make install`
  * check if it worked:
    - `saysynth --help`
  * run the tests:
    - `make test`
  * compile and view the docs:
    - `make doc && make viewdoc`


## Todo
<hr/>

### v1
- [ ] (5) Write "How to make music with saysynth" blog post.

### stretch
- [ ] (3) Fix off-by-one error in midi/arp
- [ ] (2) what to log?
- [ ] (2) Refactor Sequence into a class.

### out of scope
- [ ] (5) controls for intra-phoneme pitch modulation, eg: glide or portamento?

### done

- [x] (5) Write New Readme
- [x] (4) Write Class and CLI Documentation
- [x] (3) Add stop functionality for all commands (namespace them under `arp` etc?)
- [x] (3) Documentation Site with CI
- [x] (4) Refactor core.py
- [x] (6) Add text-to-speech in arp and midi commands
- [x] (2) Add demo command with release.
- [x] (2) Improve soundfont to include all note params
- [x] (6) Shut down certain channels in sequences
- [x] (2) Add stop all command.
- [x] (3) Figure out tempfile weirdness with prepare_options_for_say
- [x] (3) Add `render` command to `seq` which writes all tracks (including chords) to files in a directory
- [x] (3) Figure out how to suppress this error: `ImportError: sys.meta_path is None, Python is likely shutting down`
- [x] (4) Figure out why notes drop out (it's because of too many `[[ volm ]]` tags; add an option which removes these )
- [x] (3) Basic text-to-speech via text_to_phonemes
- [x] (3) add individual track launching/config overrides in seq.yml
- [x] (2) add global configs to sequence file.
- [x] (1) add more pitches to midi utils
- [x] (6) word-to-phoneme conversion
- [x] (2) Add syllable counting.
- [x] (4) arpeggiation via `midi-utils` ?
- [x] (1) custom note list for a chord
