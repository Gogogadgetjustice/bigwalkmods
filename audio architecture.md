# Audio System Architecture

This document provides an overview of the decompiled audio scripts, categorized by their structural roles and functionality within the system.

## 1. Core System & Infrastructure

Base audio management, utilities, performance culling, and signal processing tools.

* **`AudioCullable.cs`**: Registers individual audio sources to be evaluated for performance-based culling.
* **`AudioCuller.cs`**: Handles the distance or priority logic to disable or mute audio sources that are out of range or low priority.
* **`AudioDynamicReverbQualityManager.cs`**: Adjusts global or localized reverb quality dynamic settings based on performance metrics or environmental factors.
* **`AudioFilterTester.cs`**: Diagnostic or debug tool used to test and validate audio filters and DSP effects.
* **`AudioImpactConfig.cs`**: ScriptableObject or configuration asset defining impact volume thresholds and sound mappings.
* **`AudioSampleReader.cs`**: Reads raw PCM audio sample data directly from audio clips for real-time analysis or modification.
* **`AudioSampleSaver.cs`**: Saves modified or captured audio sample buffers out to assets or temporary files.
* **`AudioUtility.cs`**: Helper functions for decibel conversions, pitch variation, clipping, and audio calculations.
* **`GlobalAudioEffects.cs`**: Manages global DSP filters (e.g., low-pass filters applied during pause menus or under water).

## 2. Dynamic Impact & Physics Audio

Scripts responsible for triggering audio in response to physical collisions and dynamic movement.

* **`AudioImpactType.cs`**: Defines the `AudioImpactType` enum (`Hard`, `Soft`, `Silent`) used to classify impact intensity.
* **`AudioImpact.cs`**: Listens for physics events and evaluates collision forces to play the corresponding impact sound.
* **`CollisionSound.cs`**: Standard physical collision sound handler for environment and rigidbodies.
* **`CollisionSoundBasic.cs`**: A lightweight variant of `CollisionSound` optimized for simple objects requiring low overhead.
* **`CollisionSoundGUI.cs`**: Converts physics collision events into 2D UI audio feedback triggers.
* **`CollisionSoundGUI3D.cs`**: Triggers spatialized 3D UI audio cues based on positional interaction events.

## 3. Character & Animation Audio

Audio tied directly to entity movement, footsteps, and specific animation events.

* **`FootstepSound.cs`**: Executes footstep audio based on movement velocity and ground surface types.
* **`FootstepAudioReferences.cs`**: Container mapping surface types (e.g., dirt, metal, wood) to their respective sound banks.
* **`FootstepSoundJobScheduler.cs`**: Uses Unity's C# Job System to offload footstep distance checks and raycasts off the main thread.
* **`AnimationSound.cs`**: Animancer/Unity Animation Event listener that triggers sound effects on specific animation frames.
* **`DreamerAnimationSound.cs`**: Specialized variant of `AnimationSound` tailored for dreamer-state animation triggers.

## 4. Music & Ambience Management

Controls ambient background loops, state-based music switching, and UI music players.

* **`AmbienceSound.cs`**: Individual ambient emitter script for local environment audio loops.
* **`AmbiencePlayer.cs`**: Core controller managing ambient sound zones, crossfading, and environmental states.
* **`MusicManager.cs`**: High-level manager directing music playback, state transitions, and track queuing.
* **`MusicPlayer.cs`**: Handles low-level audio clip playback, fading, and volume control for music streams.
* **`MenuMusicPlayer.cs`**: Dedicated music player designed specifically for menu scenes and UI transitions.

## 5. Object-Specific & Mechanics Audio

Custom audio logic implemented for specific game mechanics, interactive props, or cutscenes.

* **`ChairliftAudio.cs`**: Controls loop pitching, start/stop sounds, and mechanical audio for chairlifts based on movement speed.
* **`CowbellAudio.cs`**: Specific interaction sound logic for cowbell objects.
* **`PeckEffectAudio.cs`**: Audio listener and player tailored to peck interaction mechanics.
* **`PeckEffectAudioAction.cs`**: Action trigger binding specific events to `PeckEffectAudio` execution.
* **`PeckEffectPipeVideoAudio.cs`**: Synchronizes audio playback with video stream elements during peck sequence mechanics.
