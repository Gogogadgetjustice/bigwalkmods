# Audio System Architecture

This document provides an overview of the decompiled audio scripts, categorized by their structural roles and functionality within the system.

## 1. Core System & Infrastructure

Base audio management, utilities, performance culling, and signal processing tools.

* **`AudioCullable.cs`**: Registers individual audio sources to be evaluated for performance-based culling[cite: 3].
* **`AudioCuller.cs`**: Handles the distance or priority logic to disable or mute audio sources that are out of range or low priority[cite: 3].
* **`AudioDynamicReverbQualityManager.cs`**: Adjusts global or localized reverb quality dynamic settings based on performance metrics or environmental factors[cite: 3].
* **`AudioFilterTester.cs`**: Diagnostic or debug tool used to test and validate audio filters and DSP effects[cite: 3].
* **`AudioImpactConfig.cs`**: ScriptableObject or configuration asset defining impact volume thresholds and sound mappings[cite: 3].
* **`AudioSampleReader.cs`**: Reads raw PCM audio sample data directly from audio clips for real-time analysis or modification[cite: 3].
* **`AudioSampleSaver.cs`**: Saves modified or captured audio sample buffers out to assets or temporary files[cite: 3].
* **`AudioUtility.cs`**: Helper functions for decibel conversions, pitch variation, clipping, and audio calculations[cite: 3].
* **`GlobalAudioEffects.cs`**: Manages global DSP filters (e.g., low-pass filters applied during pause menus or under water)[cite: 3].

## 2. Dynamic Impact & Physics Audio

Scripts responsible for triggering audio in response to physical collisions and dynamic movement.

* **`AudioImpactType.cs`**: Defines the `AudioImpactType` enum (`Hard`, `Soft`, `Silent`) used to classify impact intensity[cite: 3].
* **`AudioImpact.cs`**: Listens for physics events and evaluates collision forces to play the corresponding impact sound[cite: 3].
* **`CollisionSound.cs`**: Standard physical collision sound handler for environment and rigidbodies[cite: 3].
* **`CollisionSoundBasic.cs`**: A lightweight variant of `CollisionSound` optimized for simple objects requiring low overhead[cite: 3].
* **`CollisionSoundGUI.cs`**: Converts physics collision events into 2D UI audio feedback triggers[cite: 3].
* **`CollisionSoundGUI3D.cs`**: Triggers spatialized 3D UI audio cues based on positional interaction events[cite: 3].

## 3. Character & Animation Audio

Audio tied directly to entity movement, footsteps, and specific animation events.

* **`FootstepSound.cs`**: Executes footstep audio based on movement velocity and ground surface types[cite: 3].
* **`FootstepAudioReferences.cs`**: Container mapping surface types (e.g., dirt, metal, wood) to their respective sound banks[cite: 3].
* **`FootstepSoundJobScheduler.cs`**: Uses Unity's C# Job System to offload footstep distance checks and raycasts off the main thread[cite: 3].
* **`AnimationSound.cs`**: Animancer/Unity Animation Event listener that triggers sound effects on specific animation frames[cite: 3].
* **`DreamerAnimationSound.cs`**: Specialized variant of `AnimationSound` tailored for dreamer-state animation triggers[cite: 3].

## 4. Music & Ambience Management

Controls ambient background loops, state-based music switching, and UI music players.

* **`AmbienceSound.cs`**: Individual ambient emitter script for local environment audio loops[cite: 3].
* **`AmbiencePlayer.cs`**: Core controller managing ambient sound zones, crossfading, and environmental states[cite: 3].
* **`MusicManager.cs`**: High-level manager directing music playback, state transitions, and track queuing[cite: 3].
* **`MusicPlayer.cs`**: Handles low-level audio clip playback, fading, and volume control for music streams[cite: 3].
* **`MenuMusicPlayer.cs`**: Dedicated music player designed specifically for menu scenes and UI transitions[cite: 3].

## 5. Object-Specific & Mechanics Audio

Custom audio logic implemented for specific game mechanics, interactive props, or cutscenes.

* **`ChairliftAudio.cs`**: Controls loop pitching, start/stop sounds, and mechanical audio for chairlifts based on movement speed[cite: 3].
* **`CowbellAudio.cs`**: Specific interaction sound logic for cowbell objects[cite: 3].
* **`PeckEffectAudio.cs`**: Audio listener and player tailored to peck interaction mechanics[cite: 3].
* **`PeckEffectAudioAction.cs`**: Action trigger binding specific events to `PeckEffectAudio` execution[cite: 3].
* **`PeckEffectPipeVideoAudio.cs`**: Synchronizes audio playback with video stream elements during peck sequence mechanics[cite: 3].