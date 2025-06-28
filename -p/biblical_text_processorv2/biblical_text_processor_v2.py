#!/usr/bin/env python3
"""
Biblical Text Processor V2 - Multi-Section Generator
Automatically breaks large biblical text into multiple 1000-word sections for video generation.

Usage: Run the script to process text from 'Input' file into multiple video-ready sections.
Output: All processed sections saved in 'Output' file with clear separators.
"""

import re
import sys
import os

def clean_text(text):
    """Clean and normalize the input text."""
    # Remove extra whitespace and normalize line breaks
    text = re.sub(r'\n+', ' ', text)  # Replace multiple newlines with spaces
    text = re.sub(r'\s+', ' ', text.strip())  # Replace multiple spaces with single space
    
    # Remove verse references like "Deuteronomy 4:7-8" but keep the actual text
    text = re.sub(r'\b[A-Za-z]+\s+\d+:\d+(-\d+)?\s+', '', text)
    
    # Remove standalone numbers at the beginning of sentences (verse numbers)
    text = re.sub(r'\s+\d+\s+', ' ', text)
    
    # Clean up punctuation spacing
    text = re.sub(r'([.!?])\s*', r'\1 ', text)
    
    # Remove multiple spaces again
    text = re.sub(r'\s+', ' ', text)
    
    # Remove section headers and precept references (but keep main content)
    text = re.sub(r'Precepts to [^:]+:', '', text)
    text = re.sub(r'How special and Holy they are', '', text)
    text = re.sub(r'THE MOST HIGH CHOSEN PEOPLE', '', text)
    text = re.sub(r'Conclusion', '', text)
    
    return text.strip()

def split_into_words(text):
    """Split text into individual words."""
    return text.split()

def create_sections(words, max_words=1000):
    """Break words into multiple sections of max_words each."""
    sections = []
    current_section = []
    
    i = 0
    while i < len(words):
        # Add words to current section until we reach max_words
        while len(current_section) < max_words and i < len(words):
            current_section.append(words[i])
            i += 1
        
        # If we have a full section, try to end at a complete sentence
        if len(current_section) == max_words and i < len(words):
            section_text = ' '.join(current_section)
            
            # Find last complete sentence
            last_period = section_text.rfind('.')
            last_exclamation = section_text.rfind('!')
            last_question = section_text.rfind('?')
            last_sentence_end = max(last_period, last_exclamation, last_question)
            
            if last_sentence_end > len(section_text) * 0.7:  # Only if we don't cut too much
                clean_section_text = section_text[:last_sentence_end + 1]
                sections.append(clean_section_text.split())
                
                # Move remaining words to next section
                remaining_text = section_text[last_sentence_end + 1:].strip()
                current_section = remaining_text.split() if remaining_text else []
            else:
                # If no good sentence break, just use the full section
                sections.append(current_section[:])
                current_section = []
        else:
            # Add remaining words as final section
            if current_section:
                sections.append(current_section[:])
                current_section = []
    
    return sections

def format_section(words, section_num):
    """Format a single section with proper structure."""
    text = ' '.join(words)
    sentences = re.split(r'([.!?])', text)
    formatted_sentences = []
    sentence_count = 0
    
    for i in range(0, len(sentences) - 1, 2):
        if i + 1 < len(sentences):
            sentence = sentences[i] + sentences[i + 1]
            if sentence.strip():  # Only add non-empty sentences
                formatted_sentences.append(sentence.strip())
                sentence_count += 1
                
                # Add line break every 2 sentences for readability
                if sentence_count % 2 == 0:
                    formatted_sentences.append('\n')
    
    formatted_text = ''.join(formatted_sentences).strip()
    
    # Add section header
    word_count = len(words)
    expected_minutes = word_count / 150
    expected_scenes = word_count // 40
    
    section_header = f"""
=== SECTION {section_num} ===
📊 Words: {word_count} | 🎬 Est. Video: {expected_minutes:.1f} min | 🎭 Scenes: {expected_scenes}
📹 Ready for Biblical Video Generator

"""
    
    return section_header + formatted_text

def read_input_file():
    """Read content from the Input file."""
    input_file = "Input"
    
    if not os.path.exists(input_file):
        print(f"❌ Error: '{input_file}' file not found!")
        print("   Please make sure the 'Input' file exists in the current directory.")
        return None
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"❌ Error reading '{input_file}': {e}")
        return None

def save_output(sections_text):
    """Save all processed sections to Output file."""
    output_file = "Output"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sections_text)
        print(f"💾 ✅ All sections saved to: {output_file}")
        return True
    except Exception as e:
        print(f"💾 ❌ Error saving to '{output_file}': {e}")
        return False

def main():
    print("=" * 70)
    print("📖 BIBLICAL TEXT PROCESSOR V2 - MULTI-SECTION GENERATOR")
    print("=" * 70)
    print("🎯 Breaks large biblical text into multiple 1000-word sections")
    print("📹 Each section optimized for Biblical Video Generator")
    print("⏱️  Generates 5-7 minute videos per section at 150 WPM")
    print("-" * 70)
    
    print("\n📂 Reading biblical text from 'Input' file...")
    
    # Read from Input file
    raw_text = read_input_file()
    if raw_text is None:
        return
    
    print("✅ Successfully loaded text from Input file")
    print(f"📄 Raw text length: {len(raw_text)} characters")
    
    print("\n🔄 Processing text...")
    
    # Clean and process the text
    cleaned_text = clean_text(raw_text)
    words = cleaned_text.split()
    
    print(f"📊 Total word count after cleaning: {len(words)} words")
    
    if len(words) == 0:
        print("❌ No words found after cleaning. The text may need manual review.")
        return
    
    # Create sections
    sections = create_sections(words, max_words=1000)
    
    print(f"✂️  Text divided into {len(sections)} sections")
    
    # Format all sections
    all_sections_text = ""
    total_words = 0
    
    print("\n📋 SECTION BREAKDOWN:")
    print("-" * 50)
    
    for i, section_words in enumerate(sections, 1):
        word_count = len(section_words)
        expected_minutes = word_count / 150
        total_words += word_count
        
        print(f"Section {i}: {word_count} words → {expected_minutes:.1f} min video")
        
        # Format this section
        formatted_section = format_section(section_words, i)
        all_sections_text += formatted_section
        
        # Add separator between sections (except for last section)
        if i < len(sections):
            all_sections_text += "\n\n" + "="*70 + "\n\n"
    
    print("-" * 50)
    print(f"📊 TOTAL: {total_words} words across {len(sections)} sections")
    print(f"🎬 Total video time: {(total_words / 150):.1f} minutes")
    print(f"📹 Ready for {len(sections)} separate video generations")
    
    # Save to Output file
    print(f"\n💾 Saving all sections to 'Output' file...")
    
    # Add header to the output file
    output_header = f"""📖 BIBLICAL TEXT PROCESSOR V2 - PROCESSED SECTIONS
Generated: Multiple sections from large biblical text
Total Sections: {len(sections)}
Total Words: {total_words}
Total Video Time: {(total_words / 150):.1f} minutes

Instructions:
- Each section below is optimized for Biblical Video Generator
- Copy individual sections for separate video generation
- Each section generates 5-7 minutes of professional biblical video

{'='*70}

"""
    
    final_output = output_header + all_sections_text
    
    if save_output(final_output):
        print("✅ SUCCESS! All sections processed and saved.")
        print(f"\n🎯 Next Steps:")
        print(f"   1. Open the 'Output' file")
        print(f"   2. Copy Section 1 for your first video")
        print(f"   3. Paste into Biblical Video Generator")
        print(f"   4. Repeat for remaining {len(sections)-1} sections")
        print(f"\n🎬 You now have {len(sections)} video-ready biblical sections!")
    else:
        print("❌ Error occurred while saving. Please check file permissions.")

if __name__ == "__main__":
    main()