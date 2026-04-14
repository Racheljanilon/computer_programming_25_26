# SESSION 3 (Refactored into Functions)

# Constants (unchanged)
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"


# 1. Initialize metrics
def initialize_metrics():
    return 0, 0, 0, []


# 2. Create flower1 dictionary
def create_flower1():
    return {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


# 3. Create flower2 dictionary
def create_flower2():
    return {
        "id": "flower2",
        "sepal_length": 4.9,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


# 4. Create dataset list
def create_dataset(f1, f2):
    return [f1, f2]


# 5. Print sample basic info
def print_sample_info(sample):
    print(sample["id"], sample["petal_length"], sample["species"])


# 6. Predict label based on threshold
def predict_label(sample):
    if sample[FEATURE_NAME] < THRESHOLD:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL


# 7. Get true label
def get_true_label(sample):
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL


# 8. Update metrics
def update_metrics(y_pred, y_true, correct, wrong):
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    return correct, wrong


# 9. Process dataset loop
def process_dataset(dataset):
    correct, wrong, total, y_pred_list = initialize_metrics()

    print("\n=== Start session 3 Prediction Loop ===")

    for sample in dataset:
        print_sample_info(sample)

        y_pred = predict_label(sample)
        y_true = get_true_label(sample)

        correct, wrong = update_metrics(y_pred, y_true, correct, wrong)

        total += 1
        y_pred_list.append(y_pred)

        print(
            f"id={sample['id']} | true={y_true} | pred={y_pred} | "
            f"petal_length={sample['petal_length']}"
        )

    return correct, wrong, total, y_pred_list


# 10. Compute and print final metrics
def print_summary(correct, wrong, total, y_pred_list):
    accuracy = (correct / total) * 100 if total > 0 else 0.0

    print("\n=== session 3 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


# MAIN EXECUTION
flower1 = create_flower1()
flower2 = create_flower2()

dataset = create_dataset(flower1, flower2)

correct, wrong, total, y_pred_list = process_dataset(dataset)

print_summary(correct, wrong, total, y_pred_list)