import pysam

def calculate_vcf_stats(vcf_file):
    """
    Calculate various statistics from a Variant Call Format (VCF) file.

    Args:
        vcf_file (str): The path to the VCF file.

    Returns:
        None

    Prints:
        Number of variants: The total number of variants in the VCF file.
        Average VAF of heterozygous variants: The average Variant Allele Frequency (VAF) of heterozygous variants.
        Number of deletions: The total number of deletions in the VCF file.
    """
    vcf = pysam.VariantFile(vcf_file)
    total_variants = 0
    total_heterozygotes = 0
    total_vaf = 0
    total_deletions = 0

    for record in vcf:
        total_variants += 1
        genotype = record.samples[1]['GT']
        if record.samples[1]['GT'][0] != record.samples[1]['GT'][1]:
            total_heterozygotes += 1
            total_vaf += record.samples[1]['AD'][1] / record.samples[1]['DP']
        if len(record.alleles[0]) > len(record.alleles[1]):
            total_deletions += 1

    if total_heterozygotes == 0:
        average_vaf = 0
    else:
        average_vaf = total_vaf / total_heterozygotes

    print("Number of variants: ", total_variants)
    print("Average VAF of heterozygous variants: ", average_vaf)
    print("Number of deletions: ", total_deletions)

vcf_file_path = "variants.vcf"
calculate_vcf_stats(vcf_file_path)



def extract_reads_with_mapping_quality(bam_file):
    """
    Extracts reads from a BAM file that have a mapping quality over 30.

    Parameters:
        bam_file (str): The path to the BAM file.

    Returns:
        None
    """
    bam = pysam.AlignmentFile(bam_file, "rb")
    high_quality_reads = [read for read in bam if read.mapping_quality > 30]
    print("Number of reads with mapping quality over 30:", len(high_quality_reads))
        
      

def analyze_bam(bam_file):
    """
    Analyzes a given BAM file and prints the number of mapped, unmapped, and properly paired reads.

    Parameters:
    - bam_file (str): The path to the BAM file.

    Returns:
    None
    """
    bam = pysam.AlignmentFile(bam_file, "rb")
    mapped_reads = 0
    unmapped_reads = 0
    properly_paired_reads = 0

    for read in bam:
        if not read.is_unmapped:
            mapped_reads += 1
        else:
            unmapped_reads += 1

        if read.is_proper_pair:
            properly_paired_reads += 1

    print("Number of mapped reads:", mapped_reads)
    print("Number of unmapped reads:", unmapped_reads)
    print("Number of properly paired reads:", properly_paired_reads)




def filter_reads(bam_file):
    """
    Filters reads from a BAM file based on mapping quality and proper pairing.

    Parameters:
        bam_file (str): The path to the input BAM file.

    Returns:
        None
    """
    # Open the input BAM file for reading
    bam = pysam.AlignmentFile(bam_file, "rb")

    # Generate output file names
    output_file_quality = bam_file.replace(".bam", "_quality.bam")
    output_file_paired = bam_file.replace(".bam", "_paired.bam")

    # Create new BAM files for filtered reads
    output_bam_quality = pysam.AlignmentFile(output_file_quality, "wb", header=bam.header)
    output_bam_paired = pysam.AlignmentFile(output_file_paired, "wb", header=bam.header)

    # Iterate over each read in the BAM file
    for read in bam:
        # Filter reads based on mapping quality
        if read.mapping_quality > 30:
            output_bam_quality.write(read)
        # Filter reads based on proper pairing
        if not read.is_proper_pair:
            output_bam_paired.write(read)

    # Close the input and output BAM files
    bam.close()
    output_bam_quality.close()
    output_bam_paired.close()
    
filter_reads("VariantViewer_DNA.bam")
analyze_bam("VariantViewer_DNA.bam")
    